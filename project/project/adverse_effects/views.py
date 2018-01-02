import os
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from adverse_effects.forms import UserForm, AdverseEffectForm, BlogForm
from adverse_effects.models import User, Drug, AdverseEffect, Blog, Comment
from ontology.addEntries import CreateOntology
from ontology.ontologyHandler import OntologyHandler
from ontology.search import OntologySearch
from ontology import search_social as ss


def home(request):

    return render(request, "adverse_effects/home.html", context={})


def drug_list(request):
    # ontology = OntologyHandler("ontology")
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.join(path, "ontology/"))
    JsonResponse(path, safe=False)


def search_by_drug(request):
    ss.createOntology()
    ont = OntologySearch()
    results = []
    results2 = []
    type = ""
    drug = None
    drugs = ['--- select drug ---', 'Diazepam', 'EpiPen', 'Epinephrine', 'Nitroglycerin', 'Vasopressin', 'Panadol/Acetaminophen', 'Ventolin/Salbutamol', 'Aspirin', 'Zovirax/Acyclovir']


    if request.method == 'POST':
        if len(request.POST['drug']) > 2:
            drug = request.POST['drug']
        if request.POST['type'] == 'Active Ingredients':
            results = ont.searchActiveIngredientsWithDrug(drug)
        elif request.POST['type'] == 'Adverse Effects':
            results = ont.searchAdverseEffects(drug)
            results2 = ss.searchAdverseEffects(drug, 32, "male", 5, 5)

        type = request.POST['type']

    return render(request, 'adverse_effects/search-by-drug.html', context={'results': results, 'results2': results2, 'drugs': ont.getAllDrugs(), 'drug': drug, 'type': type})


def search_by_adverse_effect(request):
    ont = OntologySearch()
    results = []
    type = ""
    adverse_effect = None
    adverse_effects = ['--- select adverse effect ---', 'Asthma', 'Diabetic', 'Hypertension', 'Sweating', 'Ulcer']

    if request.method == 'POST':
        if len(request.POST['adverse_effect']) > 2:
            adverse_effect = request.POST['adverse_effect']
        if request.POST['type'] == 'Active Ingredients':
            results = ont.searchActiveIngredientsWithAdverseEffect(adverse_effect)
        elif request.POST['type'] == 'Drugs':
            results = ont.searchDrugsWithAdverseEffect(adverse_effect)
        elif request.POST['type'] == 'searchBodyPartsForAdverseEffect':
            results = ont.searchBodyPartsForAdverseEffect(adverse_effect)

        type = request.POST['type']

    return render(request, 'adverse_effects/search-adverse-effect.html', context={'results': results, 'adverse_effects': adverse_effects, 'adverse_effect': adverse_effect, 'type': type})

@login_required
def drug_details(request, id=None):
    if id:
        context = [Drug.objects.filter(id=id)]
    else:
        context = Drug.objects.all()

    q = request.GET.get('q', None)
    if q:
        context = context.filter(Q(drugname__icontains=q) | Q(adverseeffect__name__contains=q)).distinct()

    return render(request, 'adverse_effects/drug_list.html', context={'context': context, 'q': q})


@login_required
def adverse_effect(request, id=None, did=None):
    ont = OntologySearch()
    if id:
        effect = get_object_or_404(AdverseEffect, id=id)
    elif did:
        effect = AdverseEffect(drug=get_object_or_404(Drug, id=did))
    else:
        effect = None

    drug = ""
    drugs = ont.getAllDrugs()
    if request.method == 'POST':
        drug = request.POST['drug']
        name = request.POST['name']
        bodypart = request.POST['bodypart']

        if len(drug) > 2 and len(name) > 2 and len(bodypart) > 2:
            ont = CreateOntology()
            user = request.user
            sex = "male" if user.sex == "M" else "female"
            status = ont.addNewEntry(drug, name, user.id, user.username, user.age, sex, user.height, user.weight)
            if status == "Successfully Saved":
                return render(request, 'adverse_effects/adverse_effect_create.html', context={'msg': "Successfully Created", 'drugs': drugs, 'drug': drug, 'bodypart': bodypart, 'name': name})
            elif status == "The adverse effect is not on the ontology. Cannot add entry.":
                options = OntologySearch().searchAdverseEffectWithDescription(name)
                print("--------")
                print(options)
                return render(request, 'adverse_effects/adverse_effect_create.html', context={'msg': "{}. See suggestions: {}".format(status, ', '.join(options[:10])), 'drugs': drugs, 'drug': drug, 'bodypart': bodypart, 'name': name})
            else:
                return render(request, 'adverse_effects/adverse_effect_create.html', context={'msg': status, 'drugs': drugs, 'drug': drug, 'bodypart': bodypart, 'name': name})
        else:
            return render(request, 'adverse_effects/adverse_effect_create.html', context={'msg': "Form Erro ", 'drugs':drugs, 'drug': drug, 'bodypart': bodypart, 'name': name})
    else:
        form = AdverseEffectForm(instance=effect)

    return render(request, 'adverse_effects/adverse_effect_create.html', context={'form': form, 'drugs':drugs, 'drug': drug})


@login_required
def blog(request, id=None):
    if id:
        blogs = [Blog.objects.filter(id=id)]
    else:
        blogs = Blog.objects.all()

    q = request.GET.get('q', None)
    if q:
        blogs = blogs.filter(Q(content__icontains=q)).distinct()

    return render(request, 'adverse_effects/blog.html', {'blogs': blogs, 'q': q})


@login_required
def new_blog(request, id=None):
    if id:
        blog = get_object_or_404(Blog, id=id)
    else:
        blog = None

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()

            return redirect(reverse("core:home"))
    else:
        form = BlogForm(instance=blog)
    return render(request, "adverse_effects/blog-new.html", context={'form': form})


@login_required
def detail_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        comment = request.POST['comment']
        if len(comment) < 3:
            pass
        comm = Comment.objects.create(user=request.user, content=comment, blog=blog)

        return redirect(reverse("core:blog-detail", kwargs={'id': id}))

    return render(request, 'adverse_effects/blog-detail.html', {'blog': blog})


def register(request, id=None):
    if id:
        profile = get_object_or_404(User, id=id)
    else:
        profile = None

    if request.method == "POST":
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            if profile:
                created = False
                profile.email = form.cleaned_data['email']
                profile.username = form.cleaned_data['username']
                profile.first_name = form.cleaned_data['first_name']
                profile.last_name = form.cleaned_data['last_name']
                profile.sex = form.cleaned_data['sex']
                profile.age = form.cleaned_data['age']
                profile.height = form.cleaned_data['height']
                profile.weight = form.cleaned_data['weight']
                profile.credibility = form.cleaned_data['credibility']
                profile.save()
            else:
                user, created = User.objects.get_or_create(
                    email=form.cleaned_data['email'],
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'].title(),
                    last_name=form.cleaned_data['last_name'].title(),
                    sex=form.cleaned_data['sex'].title(),
                    age=form.cleaned_data['age'],
                    height=form.cleaned_data['height'],
                    weight=form.cleaned_data['weight'],
                    credibility=form.cleaned_data['credibility']
                )
            if created:
                user.set_password(form.cleaned_data['password'])  # This line will hash the password
            user.save()

            return redirect(reverse("core:home"))
    else:
        form = UserForm(instance=profile)
    return render(request, "adverse_effects/register.html", context={'form': form})

