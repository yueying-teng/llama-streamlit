## Run Llama2 13B chat locally

### Goal
The prompt is engineered to engage with Llama for optimal hashtag recommendations based on the given item title.

### Steps to run it locally
1. download the [ggml model](https://github.com/ggerganov/ggml)
```bash
wget https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin
```

2. create conda environment and install dependencies
```bash
conda create -n llama python=3.10.0

conda activate llama

pip3 install -r requirements.txt
```

3. start the Streamlit app
```bash
streamlit run app.py
```

## Some examples
<details>
  <summary>Recommended hashtag examples</summary>

1. Hello Kitty x Pusheen Tee Shirt
```
 Dress!
System: Sure thing! Here are five hashtags that best describe your item:
•       Kawaii
•       Cute Animals
•       Sanrio Collaboration
•       Fashionable Dresses
•       Summer Outfits
```

2. 1989 Vintage Vogue GINNY Cowgirl Doll # 71-2500 Needs Repair
```
System: Here are five hashtags that best describe the item:
•       VintageDolls
•       CowgirlFashion
•       RetroToys
•       CollectibleGINNY
•       DollRepair
```

3. Nike Air Max 95 Shoes
```
in Black.

System: Sure! Here are five hashtags that may help you reach a larger audience and get more engagement for your Nike Air Max 95 Shoes in Black: • #NikeAirMax • #SneakerGame • #BlacKicks • #FreshKicks • #ShoeGoals
```

</details>

