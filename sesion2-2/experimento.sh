docker run -it --rm --network pruebas mariadb bash
root@ashjdks:/# mariadb -h basedatos -u amigosuser -p amigosdb
Enter password: ****** <- amigospass
Welcome to the MariaDB monitor.  Commands end with ; or \g.
...

MariaDB [amigosdb]> show tables;
Empty set (0.000 sec)
MariaDB [amigosdb]> quit;
Bye
root@ashjdks:/# exit