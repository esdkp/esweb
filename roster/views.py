from django.shortcuts import render
from roster.models import EQCharacter, EQRace, EQClass

def roster_view(request):
    eqrace = EQRace.objects.create()
    eqclass = EQClass.objects.create()
    eqc1 = EQCharacter.objects.create(name="Hello", eqclass=eqclass, eqrace=eqrace)
    eqc2 = EQCharacter.objects.create(name="World", eqclass=eqclass, eqrace=eqrace)
    characters = EQCharacter.objects.all()
    for m in EQRace.objects.all():
        m.delete()
    for m in EQClass.objects.all():
        m.delete()
    for m in EQCharacter.objects.all():
        m.delete()
    return render(request, 'roster_view.html', {'characters': characters})
