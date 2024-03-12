from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def uslugi(request):
    first_tr = [
        ['Консультация', "300 руб.",  ""],
        ["Диагностическое вмешательство", "1 500 руб.", "1 500 руб."],
        ["Имплантация эмали (лечение кариеса)", "2 500 руб.", "2 500 руб."],
        ["Лечение поверхностного и начального кариеса",  "2 800 руб.", "3 000 руб."],
        ["Имплантация эмали (лечение кариеса)", "2 500 руб",  "2 500 руб"],
        ["Диагностическое вмешательство", "1 500 руб.", "1 500 руб."],
        ["Имплантация эмали (лечение кариеса)", "2 500 руб.", "2 500 руб."],
        ["Консультация", "300 руб.", ""]
    ]


    

    data = {"fr":first_tr}
    return render(request, 'main/uslugi.html', context=data)

def map(request):
    return render(request, 'main/map.html')
