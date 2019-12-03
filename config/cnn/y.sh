for ((i=1; i<=6; ++i))
do
    sed -i 's/SOFTMAX/SOFT-MAX/g' eb/default-"$i"eb.yaml
done
