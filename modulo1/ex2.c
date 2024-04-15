#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_occurences(char *a, char tofind);
int contains(char search, char dis[], int length);
char *read_file(char *file_name);


void count_bits(int val) {
    int count_zeros = 0;
    int count_ones = 0;

    for (int i = 0; i < sizeof(int) * 8; i++) {
        int bit = (val >> i) & 1;

        if (bit == 0) {
            count_zeros++;
        } else {
            count_ones++;
        }
    }

    // Print the results
    printf("Number of bits set to 0: %d\n", count_zeros);
    printf("Number of bits set to 1: %d\n", count_ones);
}

//2
//Função void print_fibonnaci( int N ) que imprime na consola os primeiros N termos da sequência de Fibonacci
//https://en.wikipedia.org/wiki/Fibonacci_sequence


void print_fibonnaci( int N ){

    int prev = 1;
    int curr = 1;
    int next = 0;
    int cnt = 1;
    printf("0\n");
    if(N > 1){printf("1\n");};
    

    while(cnt <= (N - 1)){
        next = prev + curr;
        prev = curr;
        curr = next;
        printf("%d\n", curr);
        cnt++;
    }
    


}

//Função int file_symbol_freq( char *file_name, char symbol ) que calcula a frequência de ocorrência do
//símbolo symbol no ficheiro file_name. A função retorna -1, caso o ficheiro não contenha qualquer ocorrência de
//symbol.

int file_symbol_freq( char *file_name, char symbol){

    char *text = read_file(file_name);
    int size = strlen(text);
    int reps =  count_occurences(text, symbol);
    free(text);

    float ret = ((float)reps / size) * 100.0;
    return ret;

}



int count_occurences(char *a, char tofind){

    int cnt = 0;
    int cnt2 = 0;
    while (a[cnt2] != '\0'){
    if(a[cnt2]== tofind){
                cnt++;
            }
        cnt2++;
    }
    return  cnt;
}

//Função void file_histogram( char *file_name ) 
//que imprime na consola o histograma dos símbolos que ocorrem no ficheiro file_name.

struct pair{
        int count;
        char letter;
    };

int count_different_char(char *a) { //funciona
    int cnt = 0;
    int z[256] = {0};

    while (*a != 0) {
        if (z[(unsigned char)*a] == 0) {
            z[(unsigned char)*a] = 1;
            cnt++;
        }
        a++;
    }
    return cnt;
}



void file_histogram( char *file_name ){
    

    char *filestr = read_file(file_name);
    int diferentletters = count_different_char(filestr);
    char visited[256] = {0};
    struct pair *pair_array = malloc(diferentletters * sizeof(struct pair));
    printf(filestr);
    int failsafe = 0;
    int cntarrvisited = 0;
    int cntarrout = 0;

    while(1){ //just in case
        ++failsafe;
        char temp = *filestr;
        int sel = contains(temp, visited, 256);
        if(sel < 1){

            visited[cntarrvisited] = temp;
            cntarrvisited++;

            pair_array[cntarrout].count = count_occurences( filestr, temp); 
             pair_array[cntarrout].letter = temp;
             cntarrout++;

        }
        //printf("%d",cntarrout);
        if(cntarrout >= diferentletters){
            break;
        }
        filestr++;
    }

    // now print it:
    for (int i = 0; i < cntarrout; ++i) {
        printf("letter: %c count: %d , ", pair_array[i].letter, pair_array[i].count);
    }
    printf("\n");
}

int contains(char search, char dis[], int length) {
    for (int i = 0; i < length; ++i) {
        if (dis[i] == search) {
            return 1;
        }
    }
    return 0;
}

char* read_file(char* file_path) {
    FILE* file = fopen(file_path, "r");
    
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* content = (char*)malloc(file_size + 1);
    if (content == NULL) {
        fclose(file);
        perror("Memory allocation error");
        exit(EXIT_FAILURE);
    }

    fread(content, 1, file_size, file);
    content[file_size] = '\0';

    fclose(file);
    return content;
}


/*Função void reverse_file( char *input_file_name, char *output_file_name), a qual transforma o ficheiro
de entrada input_file_name no ficheiro de saída output_file_name. O ficheiro de saída é produzido a partir do
ficheiro de entrada com os símbolos colocados por ordem inversa.*/

void writetofile(const char *content, const char *output_file_name) {
    FILE *file = fopen(output_file_name, "w");

    if (file == NULL) {
        file = fopen(output_file_name, "w+");
        
        if (file == NULL) {
            perror("Error opening file");
            return;
        }
    }

    fprintf(file, "%s", content);

    fclose(file);
}

void reverse_file(char *input_file_name, char *output_file_name) {
    char *content = read_file(input_file_name);
    int length = strlen(content);
    char *towrite = malloc((length + 1) * sizeof(char));
    towrite[length] = '\0';

    for (int i = 0; i < length; i++) {
        towrite[i] = content[length - 1 - i];
    }

    writetofile(towrite, output_file_name);

    free(content);
    free(towrite);
}





int main(){

//file_histogram("test.txt");
reverse_file("test.txt","reversed.txt");
}





