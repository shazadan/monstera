import matplotlib.pyplot as plt
import numpy as np

def draw_confusion_matrix(cm, target, title='Confusion matrix',
                          cmap=plt.cm.Blues,
                          cell_text_color='red'):
    """Draws a confusion matrix using matplotlib library

    Parameters
    ----------
    cm : an sklearn confusion matrix
    target: panda series representing class labels
    title: title of diagram
    cmap: matplotlib color code i.e. plt.cm.Blues
    cell_text_color: color of text within a matrix cell

    Returns
    -------
    Nothing

    Example
    -------
    # When running in IPython
    %matplotlib inline
    import pandas as pd
    from sklearn.metrics import confusion_matrix
    from monstera.visuals import draw_confusion_matrix

    cm = confusion_matrix([0,1,1,1], [0,1,0,1])
    draw_confusion_matrix(cm, pd.Series([0,0,1,1]), cell_text_color='white')
    """

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(target.unique()))
    plt.xticks(tick_marks, target.unique(), rotation=45)
    plt.yticks(tick_marks, target.unique())
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    for y in range(cm.shape[0]):
        for x in range(cm.shape[1]):
            plt.text(x, y, '%.0f' % cm[y, x],
                     horizontalalignment='center',
                     verticalalignment='center',
                     color=cell_text_color,
                     fontsize=20
                     )