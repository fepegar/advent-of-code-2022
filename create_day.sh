target=src/aoc22/day_$1
cp -r template $target
cd $target
mv day_01.py day_$1.py
sed -i "s/day_01/day_$1/g" __init__.py
