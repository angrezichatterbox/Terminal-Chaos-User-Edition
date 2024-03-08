for i in {1..10};
 do
  mkdir $i
  touch $i/.gitkeep
  for j in {1..10};
   do
    mkdir $i/$j
    touch $i/$j/.gitkeep
    cp ../../../../Desert.md $i/$j/
done
done
