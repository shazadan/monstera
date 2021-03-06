import matplotlib.pyplot as plt
import numpy as np

def draw_confusion_matrix(cm, target, title='Confusion matrix', cmap=plt.cm.Blues):
    """
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
                     color='red',
                     fontsize=20
                     )