import { showMessage, hideMessage } from "react-native-flash-message";

// ... (rest of the imports)

const App = () => (
  <React.Fragment>
    <NavigationContainer>
      {/* ... (rest of your code) */}
      <RootStack.Navigator initialRouteName="Home" headerMode="none">
        {/* ... (rest of your code) */}
      </RootStack.Navigator>
    </NavigationContainer>
    <FlashMessage position="top" />
  </React.Fragment>
);

AppRegistry.registerComponent(appName, () => App);
