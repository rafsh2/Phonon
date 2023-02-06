# Script to generate e-v.dat file which is one of the two inputs #for  phonopy-qha

for i in {01..07} #change values of i #as per your case
do
tail -n1 relax-$i/OSZICAR | awk {'print $5'} >> e-v1.dat #Collect all #the values of energies for each cell from OSZICAR and put in a #file titled e-v1.dat
done

for i in {01..07}
do
grep "volume of cell" relax-$i/OUTCAR | tail -n1 | awk {'print $5'}>> e-v2.dat #Collect all the values of volumes for each cell from #OUTCAR and put in a file titled e-v2.dat
done

paste e-v2.dat e-v1.dat > e-v-2.dat #Merge e-v1.dat and e-v2.dat #into e-v.dat

rm e-v1.dat e-v2.dat #delete e-v1.dat and e-v2.dat
