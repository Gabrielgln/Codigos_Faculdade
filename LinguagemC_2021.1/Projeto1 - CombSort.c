
#include <stdio.h>
//COMB-SORT(CODIGO)!!!
void ordenar_vetor(int v[],int t){
  int intervalo = t;
  int aux;

  while(intervalo!=1){
    intervalo = intervalo/(1.3);
    for(int i=0;i<(t-intervalo);i++){
      if(v[i]>v[i+intervalo]){
        aux=v[i+intervalo];
        v[i+intervalo]=v[i];
        v[i]=aux;
      }
    }
  }
}
//insirir o vetor
void inserir(int v[],int t){
  int i;
  printf("digite os valores do vetor:\n");
  for (i=0;i<t;i++){
    scanf("%d",&v[i]);
  }
}
//imprimir o vetor
void imprimir(int vet[], int t){
     if(t>=1){
      imprimir(vet,t-1);
      printf("%d",vet[t-1]);
    } 
}
int pesquisabinaria (int vet[], int chave, int tam)
{
     int inf = 0;     // limite inferior (o primeiro índice de vetor em C é zero          )
     int sup = tam-1; // limite superior (termina em um número a menos. 0 a 9 são 10 números)
     int meio;
     
     while (inf <= sup){
          meio = (inf + sup)/2;
          if (chave == vet[meio]){
            return meio;     
			   }
          else if (chave < vet[meio]){
            sup = meio-1;
          }
          else{
            inf = meio+1;
          }
     }
     return -1;   // não encontrado
}
int main(void){
  int tam = 5;
  int vetor[tam];
  inserir(vetor,tam);
  ordenar_vetor(vetor,tam);
  imprimir(vetor,tam);
  int i, valor;
  printf("\nQual é o valor que deseja procurar?\n");
  scanf("%d", &valor);
  int n;
  n = pesquisabinaria(vetor,valor,tam);
  if (n != -1){
    printf("Achou na posicao %d!", n);
  }
return(0);
}
