#include <stdio.h>

struct nodo{
    char dato;
    struct nodo *der;
    struct nodo *izq;
};
typedef struct nodo _nodo;

_nodo *crear(int valor){
    _nodo *nuevo;

    nuevo = (_nodo *) malloc(sizeof(_nodo));
    nuevo->dato = valor;
    nuevo->der = NULL;
    nuevo->izq = NULL;

    return nuevo;
}
