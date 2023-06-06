cat_list = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Roger",
        "breed": "Siamese",
        "adopted": False
    },
    {
        "name": "Katya",
        "breed": "Persian",
        "adopted": True
    }
]

cat_list2 = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Roger",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Katya",
        "breed": "Ragdoll",
        "adopted": True
    }
]

cat_list3 = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": True
    },
    {
        "name": "Roger",
        "breed": "Ragdoll",
        "adopted": True
    },
    {
        "name": "Katya",
        "breed": "Ragdoll",
        "adopted": True
    }
]

# Write your code here.

def cat_verify(cats):
    breed = cats[0]['breed']
    if not all(cat['breed'] == breed for cat in cats):
        return False
    
    return not all(cat['adopted'] for cat in cats)



print(cat_verify(cat_list))    # False
print(cat_verify(cat_list2))
print(cat_verify(cat_list3))