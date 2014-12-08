import re
nenc = []
mind = open("RF00059_vs_UTR_Todas_sp_unicas","r")
enco = open("UTR_Todas_sp_unicas_linea.txt","r")
extr = open("results.txt", 'w')

scre = re.compile('\d{2}[.]\d{1}')
seq = re.compile("[a-zA-Z]{3}[-][a-zA-Z]{1}[^ ]*")
lots = []
counter = 0

for line in mind:
    sreco = re.findall(scre, line)
    data = re.findall(seq, line)
    if len(sreco) > 0:
        if float(sreco[0]) >= 35.8:
            if len(lots) > 0:
                lots.append(lots[0])

delduo = list(set(lots))

for item in enco:
    nenc.append(item)

for item in delduo:
    condi = False
    for line in nenc:
        if condi:
            counter += 1
            print(str((counter/len(enco))*100)[0:5]+"% Done")
            extr.write(item + "," + line)
            condi = False
            break
        if item in line:
            condi = True

mind.close()
enco.close()
extr.close()
