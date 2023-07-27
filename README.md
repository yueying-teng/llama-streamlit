## Run Llama2 13B chat locally

### Goal
Recommend hashtags based on the item's title.

**About the prompt**
- The prompt is engineered to engage with Llama2 for optimal hashtag recommendations based on the given item title.
- Note that the length and format of response can be modified by adding the requirements to the prompt.
- However, some degradation is observed in the recommended hashtags if it's not allowed to return any explanations.

### Steps to run it locally
1. clone the repo
```bash
git clone git@github.com:yueying-teng/llama-streamlit.git
```

2. download the [ggml model](https://github.com/ggerganov/ggml)
```bash
cd llama-streamlit/models
wget https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin
```

3. create conda environment and install dependencies
```bash
conda create -n llama python=3.10.0

conda activate llama

pip3 install -r requirements.txt
```

4. start the Streamlit app
```bash
streamlit run app.py
```

5. navigate to [the app here](http://localhost:8501/)

## Some examples
<details>
  <summary>Recommended hashtag examples</summary>

1. Hello Kitty x Pusheen Tee Shirt
```
System: Sure! Here are five hashtags that could help you reach a larger audience and get more engagement for your Hello Kitty x Pusheen Tee Shirt:
• #CuteTees - This hashtag is perfect for anyone looking for adorable and stylish tee shirts. Your Hello Kitty x Pusheen design will definitely stand out among the other cute designs in this hashtag.
• #AnimalLoverApproved - This hashtag is great for animal lovers who are always on the lookout for fun and unique items featuring their favorite animals. The combination of Hello Kitty and Pusheen will definitely appeal to animal lovers!
• #FemaleFashion - This hashtag is perfect for women looking for trendy and fashionable clothing items. Your tee shirt design features two beloved characters that are sure to delight female buyers.
• #KawaiiStyle - This hashtag is great for anyone who loves all things kawaii (Japanese for "cute"). Your Hello Kitty x Pusheen tee shirt design fits perfectly into this aesthetic and will appeal to those looking for adorable and stylish items.
• #SummerVibes - This hashtag is perfect for summer-themed items that are bright, colorful, and fun. Your tee shirt design features two cute characters in a playful and cheerful setting, making it a great fit for this hashtags
```

2. 1989 Vintage Vogue GINNY Cowgirl Doll # 71-2500 Needs Repair
```
System: Sure! Here are five hashtags that could help you reach a larger audience and get more engagement for your vintage Vogue GINNY cowgirl doll:
• #VintageToys - This hashtag will help you reach people who are interested in collecting vintage toys, including dolls like yours.
• #CowgirlStyle - This hashtag is perfect for showcasing the unique and stylish design of your GINNY cowgirl doll. It will help you reach people who appreciate western-inspired fashion and collectibles.
• #VogueDolls - As the item is a vintage Vogue doll, using this hashtag will help you reach people who are specifically looking for Vogue dolls or have an interest in them.
• #RetroCollectibles - This hashtag will help you reach people who are interested in collecting retro items like your vintage GINNY cowgirl doll. It's a broad term that can encompass a wide range of retro items, so it could be beneficial to use it in conjunction with more specific hashtags.
• #DollLover - This hashtag is perfect for reaching people who are passionate about dolls and collecting them. It's a broad term that can apply to any type of doll, so it could be beneficial to use it in conjunction with more specific hashtags like #VintageToys or #CowgirlStyle
```

3. Nike Air Max 95 Shoes
```
System: Sure! Here are five hashtags that could help you reach a larger audience and get more engagement for your Nike Air Max 95 Shoes:
• #NikeAirMax - This hashtag is specific to the Nike Air Max line, which is popular among sneakerheads and running enthusiasts. Using this hashtag will help you reach a targeted audience who are interested in Nike's high-quality running shoes.
• #NikeShoes - This hashtag is more general and can be used for any type of Nike shoe. It has over 1.5 million posts, making it a great way to reach a large audience.
• #AirMax95 - This hashtag is specific to the Air Max 95 model, which is a popular choice among runners and sneaker enthusiasts. Using this hashtag will help you reach people who are specifically looking for this type of shoe.
• #ShoeGameStrong - This hashtag is more creative and can be used to showcase the style and performance of your Nike Air Max 95 shoes. It has over 10,000 posts, making it a great way to get engagement and reach a smaller but still engaged audience.
• #FreshKicks - This hashtag is more casual and can be used to showcase the latest and greatest sneakers. Using this hashtag will help you reach a younger audience who are interested in trendy and stylish footwear
```

</details>

