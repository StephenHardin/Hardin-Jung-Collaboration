from itertools import islice
f=open('Mstop_182_5_mchi_15_13TeV.txt','r')

line_list=[]

for line in f:
    strip=line.strip()
    split=strip.split()
    line_list.append(split)

#print(line_list[9])

iteration_dict={'1':[9,2],'2':[10,2],'3':[11,2],'4':[12,2],'5':[13,2],'6':[14,2],'7':[9,0.25],'8':[10,0.25],'9':[11,0.25],'10':[12,0.25],'11':[13,0.25],'12':[14,0.25]}

def split(string):
    return [char for char in string]

for j in range(1,len(iteration_dict)+1):
    for i in range(2,6):
        temp_list=split(line_list[iteration_dict[str(j)][0]][i])
        #print(temp_list)
        temp_num=temp_list[1]+temp_list[2]+temp_list[3]
        print(temp_num)
        #print(float(iteration_dict[str(j)][1]))
        temp_num=float(iteration_dict[str(j)][1])*float(temp_num)
        print(temp_num)
        temp_num=str(temp_num)
        temp_list2=split(temp_num)
        #print(temp_list2)
        if len(temp_list2)==3:
            temp_list2.append("0")
        temp_list[2]=temp_list2[2]
        temp_list[3]=temp_list2[3]
        #print(temp_list)
        joined_num="".join(temp_list)
        line_list[iteration_dict[str(j)][0]][i]=joined_num
    print(line_list[iteration_dict[str(j)][0]])

    f2=open('Mstop_182_5_mchi_15_13TeV.txt','r')

    with open("Datacard"+str(j)+".txt",'w') as output:
        for row in line_list:
            output.write(str(" ".join(row))+'\n')
            
