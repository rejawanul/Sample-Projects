import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const AgeCalculatorApp = () => {
  const [birthYear, setBirthYear] = useState('');
  const [birthMonth, setBirthMonth] = useState('');
  const [birthDay, setBirthDay] = useState('');
  const [result, setResult] = useState('');

  const calculateAge = () => {
    const birthDate = new Date(`${birthYear}-${birthMonth}-${birthDay}`);
    const today = new Date();
    const ageInMilliseconds = today - birthDate;

    const years = Math.floor(ageInMilliseconds / (365.25 * 24 * 60 * 60 * 1000));
    const remainingMilliseconds = ageInMilliseconds % (365.25 * 24 * 60 * 60 * 1000);

    const months = Math.floor(remainingMilliseconds / (30 * 24 * 60 * 60 * 1000));
    const remainingDays = Math.floor((remainingMilliseconds % (30 * 24 * 60 * 60 * 1000)) / (24 * 60 * 60 * 1000));

    setResult(`You are ${years} years, ${months} months, and ${remainingDays} days old.`);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Enter your BirthDate:</Text>
      <TextInput
        style={styles.input}
        placeholder="YYYY"
        keyboardType="numeric"
        value={birthYear}
        onChangeText={(text) => setBirthYear(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="MM"
        keyboardType="numeric"
        value={birthMonth}
        onChangeText={(text) => setBirthMonth(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="DD"
        keyboardType="numeric"
        value={birthDay}
        onChangeText={(text) => setBirthDay(text)}
      />
      <Button title="Calculate" onPress={calculateAge} />
      <Text style={styles.result}>{result}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  label: {
    fontSize: 20,
    marginBottom: 10,
  },
  input: {
    height: 40,
    width: '80%',
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingLeft: 10,
  },
  result: {
    marginTop: 20,
    fontSize: 20,
  },
});

export default AgeCalculatorApp;
