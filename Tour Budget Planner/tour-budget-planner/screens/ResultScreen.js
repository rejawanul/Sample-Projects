import React from "react";
import { View, Text, StyleSheet } from "react-native";

const ResultScreen = ({ route }) => {
  const {
    pocketMoney,
    tourBudget,
    pocketMoneyAfterTour,
    backupMoney,
    parentsShare,
  } = route.params;

  return (
    <View style={styles.container}>
      <Text>Pocket Money: {pocketMoney}</Text>
      <Text>Tour Budget: {tourBudget}</Text>
      <Text>Pocket Money After Tour: {pocketMoneyAfterTour}</Text>
      <Text>Backup Money: {backupMoney}</Text>
      <Text>Parents' Share: {parentsShare}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

export default ResultScreen;
