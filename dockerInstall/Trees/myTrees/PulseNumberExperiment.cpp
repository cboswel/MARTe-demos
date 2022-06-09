#include "mdsobjects.h"
#include "stdio.h"

using namespace MDSplus;

int main() {
	Tree *myTree = new Tree("marte_mds", -1);
	int pulseNumber = myTree->getCurrent("marte_mds");
	printf("last pulseNumber = %d\n", pulseNumber);
	pulseNumber++;
	myTree->setCurrent("marte_mds", pulseNumber);
	printf("the new pulse number is %d\n", pulseNumber);
	myTree->createPulse(pulseNumber);
	return pulseNumber;
}
