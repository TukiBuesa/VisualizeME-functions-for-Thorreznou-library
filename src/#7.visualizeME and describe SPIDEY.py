#FUNCION 7 VisualizeME and describe SPIDEY
def visualizeME_and_describe_Spidey(dataframe, save= True):
    '''
    ## IMPORTANT: This function its just for SCALED dataframe (just numeric variables).
    ## If you don't have scaled your variables, please first do it!!!
    This function  generate a polar chart with your numeric 
    variables in order to compare their means.
    ### Parameters (2):
        * dataframe: `dataframe` origin table
        * save: `bool` by default is True in order to save your graph, but if you prefer don't save it, just choose 'False'
    '''
    spidey = pd.DataFrame(dataframe.mean(), columns=['Means'])

    categories=list(dataframe.columns)
    categories+=categories[:1]
    num =len(categories)

    # variables means
    value=list(dataframe.mean())
    value+=value[:1]

    loc_label = np.linspace(start=0, stop=2*np.pi, num= num)

    plt.figure(figsize=(10,10))
    ax = plt.subplot(polar=True)
    plt.plot(loc_label, value)
    plt.fill(loc_label, value, 'blue', alpha=0.1)
    # use thetagrids to place labels at the specified angles using degrees
    lines, labels = plt.thetagrids(np.degrees(loc_label), labels=categories)

    # Comienza radar chart arriba y hacia la derecha las variables
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)

    titulo= 'SPIDEY CHART TO COMPARE MEANS OF SCALED NUMERIC VARIABLES'
    plt.title(titulo, y=1.1, fontdict={'fontsize': 18})
    plt.legend(labels=['Mean'],loc=(1, 1))

    # Save graph
    if save == True:
        path=os.path.join('visualizeME_Graphic_' + titulo.lower() + '.png')
        plt.savefig(path, format='png', dpi=300)

    # Save Table
    if save == True:
        name = 'visualizeME_table_' + titulo.lower() + '.csv'
        spidey.to_csv(name, header=True)

    plt.show()
    return display(spidey)