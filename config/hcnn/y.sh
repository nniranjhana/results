mkdir er eb db ob

for ((j=1; j<=6; j++))
do
    cp default.yaml eb/default-"$j"eb.yaml
    cp default.yaml er/default-"$j"er.yaml
done

for ((j=1; j<=6; j++))
do
    sed -i 's/bitFlip/Rand/g' er/default-"$j"er.yaml
    sed -i "s/= 1.0/= 0.$j/g" eb/default-"$j"eb.yaml
    sed -i "s/= 1.0/= 0.$j/g" er/default-"$j"er.yaml
done

cp default.yaml db/default-db.yaml
sed -i 's/errorRate/dynamicInstance/g' db/default-db.yaml

cp default.yaml ob/default-ob.yaml
sed -i 's/errorRate/oneFaultPerRun/g' ob/default-ob.yaml
