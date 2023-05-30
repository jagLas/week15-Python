# # Write your solution here.
# def check_membership(guest_name, guest_list):
#     try:
#         guest_list.index(guest_name)
#         return True
#     except:
#         return False
    
# Online solution
def check_membership(guest_name, guest_list):
    return guest_name in guest_list

guest_list = ["George", "Anthony", "Susan", "Tiffany"]
print(check_membership("Sally", guest_list))        # False
print(check_membership("Anthony", guest_list))      # True