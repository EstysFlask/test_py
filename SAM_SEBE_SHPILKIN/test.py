import urllib.request
linkos = 423406077849
for i in range(linkos, 4234060117999):
    linkos += 1
    if linkos == 423406077999:
        linkos = 4234018203461
    if linkos == 4234018203486:
        linkos = 4234018274986
    elif linkos == 4234018275097:
        linkos = 4234019279144
    elif linkos == 4234019279145:
        linkos = 4234019305840
    elif linkos == 4234019305841:
        linkos = 4234019358621
    elif linkos == 4234019358799:
        linkos = 4234019384957
    elif linkos == 4234019385020:
        linkos = 4234019422946
    elif linkos == 4234019422947:
        linkos = 4234019423185
    elif linkos == 4234019423186:
        linkos = 4234019423435
    elif linkos == 4234019423436:
        linkos = 4234019423747
    elif linkos == 4234019423748:
        linkos = 4234019424014
    elif linkos == 4234019424015:
        linkos = 4234020333475
    elif linkos == 4234020333499:
        linkos = 4234020369100
    elif linkos == 4234020369299:
        linkos = 4234020381751
    elif linkos == 4234020381799:
        linkos = 4234021266904
    elif linkos == 4234021267031:
        linkos = 4234060106594
    elif linkos == 4234060106799:
        linkos = 4234060116600
    elif linkos == 4234060116799:
        linkos = 4234060117000
    elif linkos == 4234060117999:
        break
    link = urllib.request.urlopen('http://www.krasnodar.vybory.izbirkom.ru/region/krasnodar?action=ik&vrn=' + str(linkos))
    print(linkos)
    lines = []
    yiks = []
    kras = []
    kprf = False
    checker = 0

    for line in link.readlines():
        if line.find(b'<td>') != -1: 
            lines.append(line)
        if line.find(b'<h2>') != -1:
            yiks.append(line)
        if line.find(b'<span id="address_ik">') != -1:
            kras.append(line)
    link.close()

    for i in range(len(kras)):
        kras[i] = kras[i].decode('cp1251')
        if not "город Краснодар" in kras[i] or not kras[i]:
            checker = 1

    if checker == 0:
        for i in range(len(lines)):
            lines[i] = lines[i].decode('cp1251')
            if "КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ" in lines[i]: 
                kprf = True
            
        if kprf == False: 
            if yiks:
                text = yiks[1].decode('cp1251')
                text = text[text.find("№")+0:].replace('</h2>', '').strip()
                file = open("SAM_SEBE_SHPILKIN/yik.txt", "a")
                file.write(text + ', ')
                file.close()

    