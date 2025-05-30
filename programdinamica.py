import time
import pandas as pd

# Implementação dos algoritmos de Fibonacci - Amanda Bobrzyk e Marcelo Nascimento

def fibo_rec(n, contador=0):
    if n <= 1:
        return n, contador + 1
    else:
        a, contador = fibo_rec(n - 1, contador)
        b, contador = fibo_rec(n - 2, contador)
        return a + b, contador + 1

def fibo_iter(n, contador=0):
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        contador += 1
    return f[n], contador

def lookup_fibo(f, n, contador):
    if f[n] >= 0:
        return f[n], contador + 1
    if n <= 1:
        f[n] = n
    else:
        f[n], contador = lookup_fibo(f, n - 1, contador)
        b, contador = lookup_fibo(f, n - 2, contador)
        f[n] = f[n - 1] + f[n - 2]
    return f[n], contador

def memoized_fibo(n, contador=0):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n, contador)

# Reimplementação otimizada para recursivo com memoização
def fibo_rec_memo(n, memo, contador=0):
    if n <= 1:
        return n, contador + 1
    if memo[n] is not None:
        return memo[n], contador + 1
    a, contador = fibo_rec_memo(n - 1, memo, contador)
    b, contador = fibo_rec_memo(n - 2, memo, contador)
    memo[n] = a + b
    return memo[n], contador + 1

# Teste para Fibonacci
test_values = [4, 8, 16, 32, 128, 1000, 10000]
fibo_columns = ['n', 'Fibo-Rec Result', 'Fibo-Rec Iterations', 'Fibo-Rec Time', 
                'Fibo-Iter Result', 'Fibo-Iter Iterations', 'Fibo-Iter Time', 
                'Fibo-Memoized Result', 'Fibo-Memoized Iterations', 'Fibo-Memoized Time']

results_fibo_optimized = []

for n in test_values[:4]:  # Testando para valores menores de n
    memo = [None] * (n + 1)
    
    # Fibonacci recursivo
    start_time = time.time()
    fibo_rec_res, rec_counter = fibo_rec_memo(n, memo)
    rec_time = time.time() - start_time
    
    # Fibonacci iterativo
    start_time = time.time()
    fibo_iter_res, iter_counter = fibo_iter(n)
    iter_time = time.time() - start_time
    
    # Fibonacci com memoização
    start_time = time.time()
    memoized_res, memoized_counter = memoized_fibo(n)
    memoized_time = time.time() - start_time

    results_fibo_optimized.append((n, fibo_rec_res, rec_counter, rec_time, fibo_iter_res, iter_counter, iter_time, memoized_res, memoized_counter, memoized_time))

# Gerando a tabela com pandas
fibo_df_optimized = pd.DataFrame(results_fibo_optimized, columns=fibo_columns)

# Exibindo a tabela
print(fibo_df_optimized)

# Salvando a tabela em um arquivo CSV 
fibo_df_optimized.to_csv("fibonacci_results.csv", index=False)

def edit_distance_recursive(s1, s2, i, j, contador=0):
    # Caso base: uma das strings está vazia
    if i == 0:
        return j, contador + 1
    if j == 0:
        return i, contador + 1

    # Se os caracteres forem iguais, não há custo
    if s1[i - 1] == s2[j - 1]:
        return edit_distance_recursive(s1, s2, i - 1, j - 1, contador + 1)

    # Testa todas as operações possíveis: inserção, remoção e substituição
    insert_cost, contador = edit_distance_recursive(s1, s2, i, j - 1, contador + 1)
    remove_cost, contador = edit_distance_recursive(s1, s2, i - 1, j, contador + 1)
    replace_cost, contador = edit_distance_recursive(s1, s2, i - 1, j - 1, contador + 1)

    # Retorna o menor custo entre as operações
    return 1 + min(insert_cost, remove_cost, replace_cost), contador


# Função para calcular a distância de edição e contabilizar iterações
def calculate_edit_distance(s1, s2):
    distance, iterations = edit_distance_recursive(s1, s2, len(s1), len(s2))
    return distance, iterations


# Testando os casos fornecidos
s1 = "Casablanca"
s2 = "Portentoso"
distance, iterations = calculate_edit_distance(s1, s2)
print(f"Distância de edição entre '{s1}' e '{s2}': {distance}, Iterações: {iterations}")

s1 = ("Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to "
      "simplify the build processes in the Jakarta Turbine project. There were several"
      " projects, each with their own Ant build files, that were all slightly different."
      "JARs were checked into CVS. We wanted a standard way to build the projects, a clear "
      "definition of what the project consisted of, an easy way to publish project information"
      "and a way to share JARs across several projects. The result is a tool that can now be"
      "used for building and managing any Java-based project. We hope that we have created "
      "something that will make the day-to-day work of Java developers easier and generally help "
      "with the comprehension of any Java-based project.")
s2 = ("This post is not about deep learning. But it could be might as well. This is the power of "
      "kernels. They are universally applicable in any machine learning algorithm. Why you might"
      "ask? I am going to try to answer this question in this article."
      "Go to the profile of Marin Vlastelica Pogančić"
      "Marin Vlastelica Pogančić Jun")
distance, iterations = calculate_edit_distance(s1, s2)
print(f"Distância de edição entre os textos longos: {distance}, Iterações: {iterations}")
