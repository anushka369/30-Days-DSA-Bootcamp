from collections import Counter
import sys

def user_logic(n1, flowers, n2, herbs):
    """
    Determines which flowers Lily should note down in her notebook.

    Parameters:
        n1 (int): Number of flowers in Lily's garden
        flowers (list): List of integers representing the quantities of each flower
        n2 (int): Number of herbs in Rose's garden
        herbs (list): List of integers representing the quantities of each herb

    Returns:
        list: List of integers representing flowers to note down, or [-1] if none
    """
  
    # Count occurrences of flowers and herbs
    flower_count = Counter(flowers)
    herb_count = Counter(herbs)
    
    # Filter flowers where Lily has strictly more than Rose
    result = [flower for flower in flowers if flower_count[flower] > herb_count.get(flower, 0)]
    
    return result if result else [-1]

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    n1 = int(data[0])
    flowers = list(map(int, data[1:n1+1]))
    n2 = int(data[n1+1])
    herbs = list(map(int, data[n1+2:n1+2+n2]))
    
    # Call user logic function and get the result
    result = user_logic(n1, flowers, n2, herbs)
    
    # Print the result in the required format
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
