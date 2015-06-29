from cbt2.models import  *
event_list = [line.rstrip('\n') for line in open('dbpopulator\eventlist.txt')]
for i in range(0,len(event_list)):
    Eventlist.objects.get_or_create(eventID=i+1,event_text=event_list[i])


persistentnat_list = [line.rstrip('\n') for line in open('dbpopulator\persistentnat.txt')]
for i in range(0,len(persistentnat_list)):
    Persistentnat.objects.get_or_create(persistentnatID=i+1,persistentnat_text=persistentnat_list[i])

corebelief_list = [line.rstrip('\n') for line in open('dbpopulator\Corebelief.txt')]
for i in range(0,len(corebelief_list)):
    Corebelief.objects.get_or_create(corebeliefID=i+1,corebelief_text=corebelief_list[i])

intermediatebelief_list = [line.rstrip('\n') for line in open('dbpopulator\Intermediatebelief.txt')]
for i in range(0,len(intermediatebelief_list)):
    Intermediatebelief.objects.get_or_create(intermediatebeliefID=i+1,intermediatebelief_text=intermediatebelief_list[i])
