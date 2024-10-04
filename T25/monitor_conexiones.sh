#!bin/bash
netstat -natu | grep 'ESTABLISHED'



return_code=$?

if [ $return_code -eq 0 ]; then
    echo "El comando se ejecuto sin problemas"

else
    echo "Ha ocurrido un eror, codigo de retorno: $return_code"
fi

