# Sport Style Hub - Testing Documentation

![Screenshot 2024-01-04 212742](https://github.com/magz-dev/sport-style-hub/assets/97630146/70007219-2843-4070-8816-9797db235191)

Testing was ongoing throughout the entire build. During development I made use of Googles Developer Tools to ensure everything was working as expected and to assist me with troubleshooting when things didn't work as they should.

## Automated Testing

### W3C Validator

The W3C validator was used to validate the HTML on all pages of the website. It was also used to validate CSS in the style.css file.
* [CSS](docs/testing/css.png)
* [Index Page](docs/testing/home.png)
* [Product Detail Page](docs/testing/product_detail.png)
* [Products Page HTML](docs/testing/products.png)

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.

#### bag/contexts.py
![Screenshot 2024-01-05 010727](https://github.com/magz-dev/sport-style-hub/assets/97630146/54b799b7-543b-4490-9452-93aff4e2c244)

#### bag/views.py
![Screenshot 2024-01-05 011727](https://github.com/magz-dev/sport-style-hub/assets/97630146/0c43e0d1-b25b-462f-8f1b-6c8344858c7b)

#### bag/forms.py
![Screenshot 2024-01-05 011927](https://github.com/magz-dev/sport-style-hub/assets/97630146/0fce6570-51d8-4a3f-aad7-fb2d95fd37a0)

#### bag/urls.py
![Screenshot 2024-01-05 012034](https://github.com/magz-dev/sport-style-hub/assets/97630146/1320aefe-6180-4935-95da-e014ea056ffa)

#### checkout/admin.py
![Screenshot 2024-01-05 014140](https://github.com/magz-dev/sport-style-hub/assets/97630146/7a0e6814-1cfc-484b-8e73-3b661476df4f)

#### checkout/forms.py
![Screenshot 2024-01-05 014329](https://github.com/magz-dev/sport-style-hub/assets/97630146/9bdfd29c-f402-4911-8209-79edfc4effd9)

#### checkou/model.py
![Screenshot 2024-01-05 015020](https://github.com/magz-dev/sport-style-hub/assets/97630146/470f8cc4-43cf-49a0-94b7-c98fec9d277c)

#### checkout/urls.py
![Screenshot 2024-01-05 015147](https://github.com/magz-dev/sport-style-hub/assets/97630146/4756e0fe-1121-4994-acba-3e48a43cdab0)

#### checkout/views.py
![Screenshot 2024-01-05 015426](https://github.com/magz-dev/sport-style-hub/assets/97630146/533ac7a9-391a-479f-a416-c4eb4fef7855)

#### checkout/webhook_handler.py
![Screenshot 2024-01-05 015534](https://github.com/magz-dev/sport-style-hub/assets/97630146/d15d3802-eb24-4bd7-93c8-65ccb2e34c9c)

#### checkout/webhooks.py
![Screenshot 2024-01-05 015633](https://github.com/magz-dev/sport-style-hub/assets/97630146/2e912373-8eef-4dd4-b614-2087dd68832f)

#### products/admin.py
![Screenshot 2024-01-05 015902](https://github.com/magz-dev/sport-style-hub/assets/97630146/e03ac2b9-f1eb-4a80-8a5b-8948583952d5)

#### products/forms.py
![Screenshot 2024-01-05 020345](https://github.com/magz-dev/sport-style-hub/assets/97630146/b1106dae-85fd-4650-ac1b-1e51ac3c1aad)

#### products/models.py
![Screenshot 2024-01-05 020821](https://github.com/magz-dev/sport-style-hub/assets/97630146/0bd0f277-4563-4b9b-905e-9932346ab5d2)

#### products/urls.py
![Screenshot 2024-01-05 020923](https://github.com/magz-dev/sport-style-hub/assets/97630146/199948cb-34b8-4eca-9029-a9ea307e5464)

#### products/views.py
![Screenshot 2024-01-05 021309](https://github.com/magz-dev/sport-style-hub/assets/97630146/8015f22d-65fd-4eb9-af30-b98ae34475a3)

#### profiles/forms.py
![Screenshot 2024-01-05 021416](https://github.com/magz-dev/sport-style-hub/assets/97630146/5afc6072-1acb-4cd6-95c3-956f99b30519)

#### profiles/views.py
![Screenshot 2024-01-05 021546](https://github.com/magz-dev/sport-style-hub/assets/97630146/427216ea-43d9-45fb-ae64-fe8d83aef269)

### profiles/urls.py
![Screenshot 2024-01-05 021651](https://github.com/magz-dev/sport-style-hub/assets/97630146/b266c5ff-4120-4443-9d8b-a52b3f118d86)

#### max_fitness/settings.py
![Screenshot 2024-01-05 021924](https://github.com/magz-dev/sport-style-hub/assets/97630146/22030a5d-314e-4998-9960-992f892f1b99)

#### manage.py
![Screenshot 2024-01-05 022118](https://github.com/magz-dev/sport-style-hub/assets/97630146/0633e8e0-fa22-4dc6-bbae-9631b6ed05b1)

#### env.py
![Screenshot 2024-01-05 022455](https://github.com/magz-dev/sport-style-hub/assets/97630146/bf91029b-7fd0-4492-b5b4-309381e4d314)

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results
![Screenshot 2024-01-05 023343](https://github.com/magz-dev/sport-style-hub/assets/97630146/535582e9-6795-410d-8eab-4b8523d026cb)

### Mobile Results
![Screenshot 2024-01-05 024018](https://github.com/magz-dev/sport-style-hub/assets/97630146/c670cc05-4c6d-428d-9b3b-4557ef89d0ca)

- - -

## Manual testing

### Testing User Stories

#### As a first time user:
-  I want to understand the purpose of the site immediately upon entering.
-  I want to be able to find promotional coupons.

User can immediately tell the purpose of the website and learn about special offers and promotional coupons.
  
![Screenshot 2024-01-05 032135](https://github.com/magz-dev/sport-style-hub/assets/97630146/2d0357d2-ab4c-4337-844d-66c15f885c9d)

- - -

-  I want to be able to find what I need easily and for the navigation to be easy to follow and intuitive.

User can easily search, sort products or use a navigation bar.

![Screenshot 2024-01-05 033051](https://github.com/magz-dev/sport-style-hub/assets/97630146/9fba13b2-d9cb-42a2-a78f-5b68d2f8e255)

- - -

#### As a frequent user:

-  I want to get feedback when interacting with the site.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/59fdf719-381e-40b3-9639-5bdcbeb2b745)

- - -

-  I want to be able to find out information about products.
-  I want to see ratings or reviews of a product to know more about the quality and whether it is right for me.
  
User can read product description, see ratings and reviews added by verified users.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/4c58d8cb-a18e-4be4-a267-1f139406bb7d)

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/69c8fda1-08ee-4ead-aefd-9e21f0b73337)

- - -

-  I want to be able to find and select my size.

![Screenshot 2024-01-05 103337](https://github.com/magz-dev/sport-style-hub/assets/97630146/2ec4e44e-5f23-4b9e-b2d4-02f314a1b002)

- - -

-  I want to be able to shop for multiple items at once, from across the site.
-  I want to be able to edit my shopping bag.
-  I want to know what I will be charged for delivery.
   
User can add multiple items, update the shopping bag and see if there is any delivery charge.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/87cd190b-66a1-4233-8bce-7e17de6b91b3)

- - -

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/8efbdb9b-faeb-4b21-8c08-7ccb53f23356)

- - -

#### As a user with an account:

-  I want to be able to apply a discount code to my shopping bag.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/9b6dcbb2-18b5-49dd-93c2-8ebfd1dccefc)

- - -

-  I want to see my order history.
-  I want to be able to update and save my personal information.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/1adb2f7d-bc51-496d-9dd5-a6d0ef59897d)

- - -

-  I want to leave reviews of products I have purchased.
-  I want to be able to edit my reviews.

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/8675a828-ed7b-4059-9631-ec68ebb953f9)

