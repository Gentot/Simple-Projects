#include <iostream>
#include <cstring>
using namespace std;

char letter,result;
int key, option, position;

void encryption(char x,int num){
    char alp[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    for(int i=0;i<26;i++){
		if(alp[i] == x){
			position = i;
            break;
		}
		else{continue;}
    }
    if(position+num>25){
        position=0+((position+num)-25);
        result=alp[position];
        cout<<"After encryption, the letter becomes '"<<result<<"'.";
    }
    else{
        result=alp[position+num];
        cout<<"After encryption, the letter becomes '"<<result<<"'.";
    }
}

void decryption(char x,int num){
    char alp[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    for(int i=0;i<26;i++){
		if(alp[i] == x){
			position = i;
            break;
		}
		else{continue;}
    }
    if(position-num<0){
        position=26+(position-num);
        result=alp[position];
        cout<<"After Decryption, the letter becomes '"<<result<<"'.";
    }
    else{
        result=alp[position-num];
        cout<<"After Decryption, the letter becomes '"<<result<<"'.";
    }
}


int main(){
    cout<<"Please choose (1) Encryption or (2) Decryption: ";
    cin>>option;
    while(option != 1 && option != 2){
        cout<<"Invalid option. Please choose (1) Encryption or (2) Decryption.";
        cin>>option;
    }
    cout<<"Please enter an english letter: ";
    cin>>letter;
    cout<<"Please enter a key: ";
    cin>>key;
    
        if (option==1){
            encryption(letter, key);
        }
        else if(option == 2){
            decryption(letter, key);
        }
}