import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

import { showMessage, hideMessage } from "react-native-flash-message";

const BudgetCalculatorApp = () => {
  const [totalAmount, setTotalAmount] = useState("");

  const calculateBudget = () => {
    try {
      const amount = parseFloat(totalAmount);

      if (isNaN(amount)) {
        showMessage({
          message: "Error",
          description: "Please enter a valid total amount.",
          type: "danger",
        });
        return;
      }

      const tourBudget = amount * 0.02;
      const pocketMoney = amount * 0.03;
      const backupMoney = amount * 0.03;
      const internetBill = 500;
      const parentsShare =
        amount - (tourBudget + pocketMoney + backupMoney + internetBill);

      showMessage({
        message: "Result",
        description:
          `Tour Budget (2%): ${tourBudget.toFixed(2)} Taka\n` +
          `Pocket Money (3%): ${pocketMoney.toFixed(2)} Taka\n` +
          `Backup Money (3%): ${backupMoney.toFixed(2)} Taka\n` +
          `Internet Bill: ${internetBill.toFixed(2)} Taka\n` +
          `Parents Share: ${parentsShare.toFixed(2)} Taka`,
        type: "info",
      });
    } catch (error) {
      showMessage({
        message: "Error",
        description: "An error occurred. Please try again.",
        type: "danger",
      });
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Total Amount:</Text>
      <TextInput
        style={styles.input}
        value={totalAmount}
        onChangeText={setTotalAmount}
        keyboardType="numeric"
      />
      <Button title="Calculate" onPress={calculateBudget} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  label: {
    fontSize: 18,
    marginBottom: 10,
  },
  input: {
    width: 200,
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
  },
});

export default BudgetCalculatorApp;
