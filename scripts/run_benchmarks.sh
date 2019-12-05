# Error rates from 0.1 to 0.6, bitFlip-element
for ((i=1; i<=6; i++))
do
    python ./benchmarks/supervised/cnn/highway-cnn.py ./confFiles/eb/default-"$i"eb.yaml ./results/eb/
done

# Error rates from 0.1 to 0.6, Rand-element
for ((i=1; i<=6; i++))
do
    python ./benchmarks/supervised/cnn/highway-cnn.py ./confFiles/er/default-"$i"er.yaml ./results/er/
done

# Dynamic/OneFaultPerRun, bitFlip-element/Rand-element combos
python ./benchmarks/supervised/cnn/highway-cnn.py ./confFiles/db/default.yaml ./results/db/
python ./benchmarks/supervised/cnn/highway-cnn.py ./confFiles/dr/default.yaml ./results/dr/
