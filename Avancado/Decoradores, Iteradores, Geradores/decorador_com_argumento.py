import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)       
        return resultado
    return envelope

@duplicar
def aprender(tecnologia1, tecnologia2):
    print(f"Estou aprendendo {tecnologia1} e {tecnologia2}")
    return tecnologia1.upper(), tecnologia2.upper()

tecnologia = aprender("Python", "Java")
print(tecnologia)

print(aprender.__name__)