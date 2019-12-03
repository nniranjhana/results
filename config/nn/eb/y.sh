for ((i=2; i<=6; ++i))
do
    sed -i "s/= 0.1/= 0.$i/g" default-"$i"eb.yaml
done
