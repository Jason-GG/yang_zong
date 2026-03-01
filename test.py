import requests
import json
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.




# g_url = "https://www.instagram.com/api/v1/friendships/4013697812/followers/"
g_url = "https://i.instagram.com/api/v1/users/web_profile_info/?username=jardinpriveparis"

def make_request_ins():
    params = {
        "count": 12,
        "search_surface": "follow_list_page", #search_surface=follow_list_page
        "max_id": 48
    }

    # headers = {
    #     "User-Agent": "Mozilla/5.0",
    #     "Accept": "application/json",
    #     "cookie": 'datr=mE9RaCQ_gzRvnsofR9NFD-w4; ig_did=DE72CBB3-64DE-4566-9414-53E1503C2A72; mid=aFFPmAAEAAFjt-5W5PhYiJD7jTTF; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=1Y5SrUw9NunThE6IgzGQ6UoOqNa6anCq; ds_user_id=46337139866; sessionid=46337139866%3AstP0cnIJmasRnN%3A9%3AAYhZVBc6s_kz3bPRy4CgspFWsNjTLAbT8xetalJ4pCs; wd=1920x494; rur="SNB\05446337139866\0541803646346:01fec43db88cd7bd6f4fa058466f28f44a7894e4c0f0b4f77f97cb32f3577bd9e99fdc34"',
    #     "x-web-session-id": "42crck:mwlwrv:n53h1b",
    #     "x-ig-app-id": "936619743392459",
    #     "x-ig-www-claim": "hmac.AR1NsV6xVrDNIlhZkXGy7oRvZvmEu94pU-0ukA0p9Y5mHUJj"
    # }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Accept": "application/json",
        # "cookie": 'datr=mE9RaCQ_gzRvnsofR9NFD-w4; ig_did=DE72CBB3-64DE-4566-9414-53E1503C2A72; mid=aFFPmAAEAAFjt-5W5PhYiJD7jTTF; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=1Y5SrUw9NunThE6IgzGQ6UoOqNa6anCq; ds_user_id=46337139866; wd=1920x1055; sessionid=46337139866%3AstP0cnIJmasRnN%3A9%3AAYjBgW_JW59nzEGPnMxJCLRvc304ZhEyEYMf3tyoT0Y; rur="CCO\05446337139866\0541803848869:01febeb857fb9e8e81cf6d10611a9587eac3057683dbd75663c3f635e999b50e667e8f64"',
        "cookie": 'datr=mE9RaCQ_gzRvnsofR9NFD-w4; ig_did=DE72CBB3-64DE-4566-9414-53E1503C2A72; mid=aFFPmAAEAAFjt-5W5PhYiJD7jTTF; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=1Y5SrUw9NunThE6IgzGQ6UoOqNa6anCq; ds_user_id=46337139866; sessionid=46337139866%3AstP0cnIJmasRnN%3A9%3AAYjBgW_JW59nzEGPnMxJCLRvc304ZhEyEYMf3tyoT0Y; wd=1920x486; rur="CCO\05446337139866\0541803851338:01fe811412b3989aa4acdc0fd969e4bc1ee366922ccedba85d0f1d75bb54856dc6f7d092"',
        "x-ig-app-id": "936619743392459",
        "x-asbd-id": "198387",
        # "sec-fetch-storage-access": "active",
        # "sec-fetch-mode": "cors",
        # "priority": "u=1, i"
    }

    response = requests.get(g_url, params=params, headers=headers)
    # res = json.loads(response.text)
    print("Status Code:", response.status_code)
    print("Response Text:")
    print(response)
    # res = json.loads(response.text)
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    res = make_request_ins()
    print(res.text)
    iCount = 0
    # for u in res["users"]:
    #     iCount = iCount + 1
    #     print(f"======>> iCount: {iCount}")
    #     print(u)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
