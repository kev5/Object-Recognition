from xml.dom import minidom
import xml.etree.ElementTree as ET
import glob
import pandas as pd

filelist = glob.glob("./*.xml")

def bound(xml):
    xml_list = []
    tree = ET.parse(xml)#'scene.xml'
    root = tree.getroot()

    file_name = root.find('filename').text
    rows = root.find('imagesize').find('nrows').text
    cols = root.find('imagesize').find('ncols').text

    for child in root.iter('object'):
        x = []
        y = []
        classs = child.find('name').text.strip()
        for child in child.iter('pt'):
            x.append(int(child.find('x').text))
            y.append(int(child.find('y').text))
            
        value = (file_name,
                 rows,
                 cols,
                 classs,
                 min(x),
                 min(y),
                 max(x),
                 max(y))
        # print(value)
        xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return (xml_df)

def main():
    xml_df = bound(filelist[0])
    newname = str(filelist[0].replace(".xml",""))
    xml_df.to_csv((newname+'_labels.csv'), index=None)
    print('Successfully converted xml to csv.')

if __name__ == "__main__":
    main()

