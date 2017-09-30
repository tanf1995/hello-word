#include <iostream>
using namespace std;

void ReplaceBlank(char string[], int length);

int main(){
	char st[20] = "hello world tf!";

	cout<<"替换前字符串为："<<st<<"\n";
	ReplaceBlank(st,20);
	cout<<"替换后字符串为："<<st<<"\n";

	return 0;
}

/*length 为字符数组string总容量*/
void ReplaceBlank(char string[], int length){
	if(string == NULL||length <= 0){
		return;
	}

	int originaLength = 0;
	int numberOfBlank = 0;
	int i = 0;

	while(string[i] != '\0'){
		++ originaLength;

		if(string[i] == ' '){
			++ numberOfBlank;
		}

		++ i;
	}

	int newLength = originaLength + numberOfBlank*2;
	if(newLength > length){
		return;
	}

	int indexOfOriginal = originaLength;
	int indexOfNew = newLength;
	while(indexOfOriginal >= 0 && indexOfNew > indexOfOriginal){
		if(string[indexOfOriginal] == ' '){
			string[indexOfNew --] = '0';
			string[indexOfNew --] = '2';
			string[indexOfNew --] = '%';
		}
		else{
			string[indexOfNew --] = string[indexOfOriginal];
		}

		-- indexOfOriginal;
	}
}

