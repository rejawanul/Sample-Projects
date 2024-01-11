import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [totalAmount, setTotalAmount] = useState('');

  const calculateExpenses = () => {
    // Implement your expense calculation logic here
    // For simplicity, let's assume totalAmount is a valid number

    const pocketMoney = (5 / 100) * totalAmount;
    const tourBudget = (30 / 100) * totalAmount;
    const pocketMoneyAfterTour = (70 / 100) * pocketMoney;
    const backupMoney = (5 / 100) * totalAmount;
    const parentsShare = totalAmount - (pocketMoney + tourBudget + pocketMoneyAfterTour + backupMoney);

    navigation.navigate('Result', {
      pocketMoney,
      tourBudget,
      pocketMoneyAfterTour,
      backupMoney,
      parentsShare,
    });
  };

  return (
    <View style={styles.container}>
      <Text>Total Amount:</Text>
      <TextInput
        style={styles.input}
        keyboardType="numeric"
        placeholder="Enter Total Amount"
        value={totalAmount}
        onChangeText={(text) => setTotalAmount(text)}
      />
      <Button title="Calculate" onPress={calculateExpenses} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    padding: 10,
    width: 200,
  },
});

export default HomeScreen;
