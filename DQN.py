from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten
#from keras.initializers import glorot_normal
from keras.optimizers import Adam

def create_dqn(learn_rate, input_dims, n_actions, conv_units, dense_units):
    model = Sequential([
                Conv2D(conv_units, (3,3), activation='relu', padding='same', input_shape=input_dims),
                Conv2D(conv_units, (3,3), activation='relu', padding='same'),
                Conv2D(conv_units, (3,3), activation='relu', padding='same'),
                Conv2D(conv_units, (3,3), activation='relu', padding='same'),
                Flatten(),
                Dense(dense_units, activation='relu'),
                Dense(dense_units, activation='relu'),
                Dense(n_actions, activation='linear')])

    model.compile(optimizer=Adam(lr=learn_rate, epsilon=1e-4, clipnorm=0.1), loss='mse')

    return model
