#Property of Not Real Engineering 
#Copyright 2020 Not Real Engineering - All Rights Reserved You may not use, 
#           distribute and modify this code without the written permission 
#           from Not Real Engineering.
############################################################################
##             Reading the ODB file                                       ##
############################################################################


from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import random
from array import *
from odbAccess import openOdb
import odbAccess
import math
import numpy    
import os        # Operating system
import shutil    # copying or moving files

#Open text file to write results
sortie = open('Results_fromODB.txt' , 'w')
sortie.write('\t Property of Not Real Engineering')
sortie.write('\n')

odbname='Random_inclusions'         # set odb name here
path='./'                    # set odb path here (if in working dir no need to change!)
myodbpath=path+odbname+'.odb'    
odb=openOdb(myodbpath)

All_points = odb.steps['Step-1'].frames[-1].fieldOutputs['S'].values
Mises_stress_list = [];
for q in range (1,len(All_points)):
    Mises_stress = All_points[q].mises    # S11 = data[0]
    Mises_stress_list.append(Mises_stress);

Max_Mises_stress = max(Mises_stress_list);
sortie.write('Maximum Mises stress in RVE is %f \n' %Max_Mises_stress)

odb.close()
     
sortie.close()    

#Property of Not Real Engineering 
