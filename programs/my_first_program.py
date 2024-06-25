from nada_dsl import *


def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    # Define secret inputs for both parties
    my_int1_party1 = SecretInteger(Input(name="my_int1_party1", party=party1))
    my_int2_party1 = SecretInteger(Input(name="my_int2_party1", party=party1))
    
    my_int1_party2 = SecretInteger(Input(name="my_int1_party2", party=party2))
    my_int2_party2 = SecretInteger(Input(name="my_int2_party2", party=party2))
    
    # Compute the sum and product for party1
    sum_party1 = my_int1_party1 + my_int2_party1
    product_party1 = my_int1_party1 * my_int2_party1
    
    # Compute the sum and product for party2
    sum_party2 = my_int1_party2 + my_int2_party2
    product_party2 = my_int1_party2 * my_int2_party2
    
    # Compute the combined sum and product
    combined_sum = sum_party1 + sum_party2
    combined_product = product_party1 * product_party2
    
    # Determine if the combined sum is greater than the combined product
    is_sum_greater_than_product = combined_sum > combined_product
    
    # Output the results for both parties
    return [
        Output(sum_party1, "sum_party1", party1),
        Output(product_party1, "product_party1", party1),
        Output(sum_party2, "sum_party2", party2),
        Output(product_party2, "product_party2", party2),
        Output(is_sum_greater_than_product, "is_sum_greater_than_product", party1),
        Output(is_sum_greater_than_product, "is_sum_greater_than_product", party2)
    ]
