for ip in `cat ips.txt`; do
    echo $ip
    curl -I $ip -m 3
done

