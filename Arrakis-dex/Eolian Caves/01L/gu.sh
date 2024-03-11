d=$(find "./" -type d)
for i in $d;do
	echo "$i"
	touch $i/.gitkeep
done
