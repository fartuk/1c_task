import argparse
from model import TextStyleModel


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('--txt_path', type=str)
    args = parser.parse_args()
    
    style_model = TextStyleModel()
    classes = ['техническая литература', 'художественная литература', 'разговорный стиль']
    with open(args.txt_path) as f:
        text = f.read()
        
    pred = style_model.predict([text])[0]
    for style, proba in zip(classes, pred):
        print('{}:{}'.format(style, proba))
    