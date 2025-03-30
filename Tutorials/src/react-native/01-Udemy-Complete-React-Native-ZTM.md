# UDEMY-COMPLETE REACT NATIVE IN 2023 - ZTM

## [COURSES](https://www.udemy.com/course/complete-react-native-mobile-development-zero-to-mastery-with-hooks/)

<details>
  <summary>1. Introduction - Using Expo </summary>

# Using Expo

https://snack.expo.dev/

![](https://github.com/omeatai/My-Tutorials/assets/32337103/fbb5bbfb-7e94-465b-bc45-f3ffdada2f5c)

```js
import React from "react";
import { Text, View } from "react-native";

const YourApp = () => {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Helloooooo 🎉</Text>
    </View>
  );
};

export default YourApp;
```

![](https://github.com/omeatai/My-Tutorials/assets/32337103/c2011efe-a102-4cf7-aedb-1191bd097af9)

```js
import { Text, View, StyleSheet } from "react-native";
import Constants from "expo-constants";

// You can import from local files
import AssetExample from "./components/AssetExample";

// or any pure javascript modules available in npm
import { Card } from "react-native-paper";

export default function App() {
  const name = "Ifeanyi";
  return (
    <View style={styles.container}>
      <Text style={styles.paragraph}>
        {2 ** 4}Hello, my name is {name}
      </Text>
      <Card>
        <AssetExample />
      </Card>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    paddingTop: Constants.statusBarHeight,
    backgroundColor: "#ecf0f1",
    padding: 8,
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: "bold",
    textAlign: "center",
  },
});
```

# #End

</details>

<details>
  <summary>2. Install expo and React Native Project </summary>

# Install expo and React Native Project

![](https://github.com/omeatai/My-Tutorials/assets/32337103/03c2960a-55a5-4d57-bf39-3653173cd91a)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/d2002d17-d70d-4028-811a-673420f29911)

# Install expo globally

```jsbs
npm install -g expo-cli
```

# Install React Native Project

```jsbs
npx create-expo-app FocusTime
cd FocusTime
npx expo start

yarn create expo-app FocusTime
cd FocusTime
yarn expo start
```

### react-native/FocusTime/package.json:

```js
{
  "name": "focustime",
  "version": "1.0.0",
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "expo": "~48.0.18",
    "expo-status-bar": "~1.4.4",
    "react": "18.2.0",
    "react-native": "0.71.8"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  },
  "private": true
}
```

### react-native/FocusTime/App.js:

```js
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Hello World! Welcome to Android!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  text: {
    fontSize: 42,
    textAlign: "center",
    fontWeight: "700",
  },
});
```

# #End

</details>

<details>
  <summary>3. Using SafeAreaView(For IOS), Platform, StatusBar </summary>

# Using SafeAreaView(For IOS), Platform, StatusBar

![](https://github.com/omeatai/My-Tutorials/assets/32337103/81e7fda3-e6fd-43e1-b244-35e2fba8549b)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/93acb5d1-8e2f-48b1-ae8f-cabaf81faeec)

### react-native/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text>Hello World! Welcome to Android!</Text>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    // paddingTop: Platform.OS === "android" ? 20 : 0,
  },
});
```

# #End

</details>

<details>
  <summary>4. Style App Background </summary>

# Style App Background

![](https://github.com/omeatai/My-Tutorials/assets/32337103/df9e932c-c4d4-46d9-9d7d-0da4e62802ec)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/5c86283c-775d-4d40-a075-b8e3e372d435)

### react-native/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import styles from "./App.styles";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>Hello World! Welcome to Android!</Text>
    </SafeAreaView>
  );
}
```

### react-native/FocusTime/App.styles.js:

```js
import { StyleSheet, Platform, StatusBar } from "react-native";
import colors from "./src/utils/colors";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.darkPurple,
  },
  text: {
    color: colors.white,
  },
});

export default styles;
```

### react-native/FocusTime/src/utils/colors.js:

```js
const colors = {
  dodgerBlue: "#1e90ff",
  crimson: "#dc143c",
  darkPurple: "#4d004d",
  white: "#fff",
  black: "#000",
  primary: "#1e90ff",
  secondary: "#000",
};

export default colors;
```

# #End

</details>

<details>
  <summary>5. Create Focus Feature (Component) </summary>

# Create Focus Feature (Component)

![](https://github.com/omeatai/My-Tutorials/assets/32337103/3e959daa-ab07-4ad7-adcf-adb358ad7b45)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/87b8d21d-eceb-4d82-9f9b-c31d641c83fe)

### react-native/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      <Focus />
    </SafeAreaView>
  );
}
```

### react-native/FocusTime/App.styles.js:

```js
import { StyleSheet, Platform, StatusBar } from "react-native";
import colors from "./src/utils/colors";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  text: {
    color: colors.white900,
    paddingBottom: 20,
    paddingLeft: 20,
    fontWeight: Platform.OS === "android" ? "normal" : "400",
  },
});

export default styles;
```

### react-native/FocusTime/src/features/Focus.js:

```js
import React from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import colors from "../utils/colors";

const Focus = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Focus Component</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  text: {
    color: colors.black100,
  },
});

export default Focus;
```

### react-native/FocusTime/src/utils/colors.js:

```js
const colors = {
  dodgerBlue: "#1e90ff",
  crimson: "#dc143c",
  purple: "#800080",
  darkPurple: "#4d004d",
  white: "#fff",
  white900: "#858585",
  black: "#000",
  black500: "#292929",
  black200: "#5c5c5c",
  black100: "#7a7a7a",
  primary: "#1e90ff",
  secondary: "#000",
};

export default colors;
```

# #End

</details>

<details>
  <summary>6. Create Text Input with React Native Paper </summary>

# Create Text Input with React Native Paper

![](https://github.com/omeatai/My-Tutorials/assets/32337103/c2dff748-d754-4017-b540-49c9bebe5f22)

# Install React Native Paper

```jsbs
npm install react-native-paper react-native-safe-area-context

npm install react-native-paper
npm install react-native-safe-area-context

npx pod-install
npm install react-native-vector-icons
```

```js
{
  "dependencies": {
  "expo-constants": "~12.1.3",
  "@expo/vector-icons": "^12.0.0",
  "react-native-paper": "4.11.2"
  }
}
```

### react-native/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      <Focus />
    </SafeAreaView>
  );
}
```

### react-native/FocusTime/App.styles.js:

```js
import { StyleSheet, Platform, StatusBar } from "react-native";
import colors from "./src/utils/colors";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  text: {
    color: colors.white900,
    paddingBottom: 20,
    paddingLeft: 20,
    fontWeight: Platform.OS === "android" ? "normal" : "400",
  },
});

export default styles;
```

### react-native/FocusTime/src/features/Focus.js:

```js
import React from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";

const Focus = () => {
  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={"What task would you like to do?"}
          style={styles.text}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    flex: 0.5,
    padding: 20,
    justifyContent: "flex-start",
  },
  text: {
    color: colors.black100,
    borderBottomLeftRadius: 10,
    borderBottomRightRadius: 10,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    overflow: "hidden",
  },
});

export default Focus;
```

### react-native/FocusTime/src/utils/colors.js:

```js
const colors = {
  dodgerBlue: "#1e90ff",
  crimson: "#dc143c",
  purple: "#800080",
  darkPurple: "#4d004d",
  white: "#fff",
  white900: "#858585",
  black: "#000",
  black500: "#292929",
  black200: "#5c5c5c",
  black100: "#7a7a7a",
  primary: "#1e90ff",
  secondary: "#000",
};

export default colors;
```

# #End

</details>

<details>
  <summary>7. Storing Values with useState </summary>

# Storing Values with useState

![](https://github.com/omeatai/My-Tutorials/assets/32337103/c4e08684-1498-4d68-b467-c513f815ef8a)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/b59fd227-3288-4ff9-a7a3-dfbc370a6ad1)

### rn/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      <Focus />
    </SafeAreaView>
  );
}
```

### rn/FocusTime/App.styles.js:

```js
import { StyleSheet, Platform, StatusBar } from "react-native";
import colors from "./src/utils/colors";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  text: {
    color: colors.white900,
    paddingBottom: 20,
    paddingLeft: 20,
    fontWeight: Platform.OS === "android" ? "normal" : "400",
  },
});

export default styles;
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";

const Focus = () => {
  const [subject, setSubject] = useState("");

  const Label = <Text color={"#000"}>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.text}
          onChangeText={(e) => setSubject(e)}
        />
        <Text style={styles.subject}>{subject}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    flex: 0.5,
    padding: 20,
    justifyContent: "flex-start",
  },
  text: {
    color: colors.black100,
    borderBottomLeftRadius: 10,
    borderBottomRightRadius: 10,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    overflow: "hidden",
  },
  subject: {
    fontSize: 30,
    color: colors.white,
  },
});

export default Focus;
```

### rn/FocusTime/src/utils/colors.js:

```js
const colors = {
  dodgerBlue: "#1e90ff",
  crimson: "#dc143c",
  purple: "#800080",
  darkPurple: "#4d004d",
  white: "#fff",
  white900: "#858585",
  black: "#000",
  black500: "#292929",
  black200: "#5c5c5c",
  black100: "#7a7a7a",
  primary: "#1e90ff",
  secondary: "#000",
};

export default colors;
```

# #End

</details>

<details>
  <summary>8. Adding a Button </summary>

# Adding a Button

![](https://github.com/omeatai/My-Tutorials/assets/32337103/dbad6221-0eac-49fc-9de2-c6dd9c09337a)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/6d853177-88fe-4054-a6b6-20c18d195b39)

### rn/FocusTime/App.js:

```js
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      <Focus />
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";
import { RoundedButton } from "../components/RoundedButton";

const Focus = () => {
  const [subject, setSubject] = useState("");

  const Label = <Text>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.textInput}
          onChangeText={(e) => setSubject(e)}
        />
        <View style={styles.button}>
          <RoundedButton title={"+"} size={50} />
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    padding: 20,
    justifyContent: "flex-start",
    flexDirection: "row",
  },
  textInput: {
    flex: 1,
    marginRight: 10,
    color: colors.black100,
    borderBottomLeftRadius: 10,
    borderBottomRightRadius: 10,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    overflow: "hidden",
  },
  button: {
    justifyContent: "center",
  },
});

export default Focus;
```

### rn/FocusTime/src/components/RoundedButton.js:

```js
import React from "react";
import { TouchableOpacity, Text, StyleSheet } from "react-native";
import colors from "../utils/colors";

export const RoundedButton = ({
  style = {},
  textStyle = {},
  size = 125,
  ...props
}) => {
  return (
    <TouchableOpacity
      style={[styles(size).radius, style]}
      onPress={props.onPress}
    >
      <Text style={[styles(size).text, textStyle]}>{props.title}</Text>
    </TouchableOpacity>
  );
};

const styles = (size) => ({
  radius: {
    borderRadius: size / 2,
    width: size,
    height: size,
    alignItems: "center",
    justifyContent: "center",
    borderColor: colors.white,
    borderWidth: 2,
  },
  text: { color: colors.white, fontSize: size / 3 },
});
```

# #End

</details>

<details>
  <summary>9. Passing Values to App Component </summary>

# Passing Values to App Component

![](https://github.com/omeatai/My-Tutorials/assets/32337103/d0176589-300a-4b38-824b-fbfd4bfb6d34)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/591655f6-c948-4b4b-a877-066c7cb7825f)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState(null);

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <Focus addSubject={setCurrentSubject} />
      ) : (
        <View>
          <Text style={styles.text}>
            I am going to render the timer for {currentSubject}
          </Text>
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";
import { RoundedButton } from "../components/RoundedButton";

const Focus = ({ addSubject }) => {
  const [subject, setSubject] = useState("");

  const Label = <Text>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.textInput}
          onChangeText={(e) => setSubject(e)}
        />
        <View style={styles.button}>
          <RoundedButton
            title={"+"}
            size={50}
            onPress={() => addSubject(subject)}
          />
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    padding: 20,
    justifyContent: "flex-start",
    flexDirection: "row",
  },
  textInput: {
    flex: 1,
    marginRight: 10,
    color: colors.white900,
    borderBottomLeftRadius: 10,
    borderBottomRightRadius: 10,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    overflow: "hidden",
  },
  button: {
    justifyContent: "center",
  },
});

export default Focus;
```

### rn/FocusTime/src/components/RoundedButton.js:

```js
import React from "react";
import { TouchableOpacity, Text, StyleSheet } from "react-native";
import colors from "../utils/colors";

export const RoundedButton = ({
  style = {},
  textStyle = {},
  size = 125,
  ...props
}) => {
  return (
    <TouchableOpacity
      style={[styles(size).radius, style]}
      onPress={props.onPress}
    >
      <Text style={[styles(size).text, textStyle]}>{props.title}</Text>
    </TouchableOpacity>
  );
};

const styles = (size) => ({
  radius: {
    borderRadius: size / 2,
    width: size,
    height: size,
    alignItems: "center",
    justifyContent: "center",
    borderColor: colors.white,
    borderWidth: 2,
  },
  text: { color: colors.white, fontSize: size / 3 },
});
```

# #End

</details>

<details>
  <summary>10. Setting Spacing and Sizes </summary>

# Setting Spacing and Sizes

![](https://github.com/omeatai/My-Tutorials/assets/32337103/2fe7b4e2-0c5e-4e5e-8d90-912af52d747c)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/85225443-d58d-4e0c-abc7-3ac18fd6799a)

### rn/FocusTime/src/utils/sizes.js:

```js
export const fontSizes = {
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 40,
  xxxl: 80,
};

export const spacing = {
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 40,
  xxxl: 80,
};
```

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState(null);

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <Focus addSubject={setCurrentSubject} />
      ) : (
        <View>
          <Text style={styles.text}>
            I am going to render the timer for {currentSubject}
          </Text>
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";
import { spacing, fontSizes } from "../utils/sizes";
import { RoundedButton } from "../components/RoundedButton";

const Focus = ({ addSubject }) => {
  const [subject, setSubject] = useState("");

  const Label = <Text>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.textInput}
          onChangeText={(e) => setSubject(e)}
        />
        <View style={styles.button}>
          <RoundedButton
            title={"+"}
            size={50}
            onPress={() => addSubject(subject)}
          />
        </View>
      </View>
    </View>
  );
  Ω;
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    padding: spacing.lg,
    justifyContent: "flex-start",
    flexDirection: "row",
  },
  textInput: {
    flex: 1,
    marginRight: spacing.sm,
    color: colors.white900,
    borderBottomLeftRadius: spacing.sm,
    borderBottomRightRadius: spacing.sm,
    borderTopLeftRadius: spacing.sm,
    borderTopRightRadius: spacing.sm,
    overflow: "hidden",
  },
  button: {
    justifyContent: "center",
  },
});

export default Focus;
```

# #End

</details>

<details>
  <summary>11. Create CountDown Component</summary>

# Create CountDown Component

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import { colors } from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);
export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd();
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;
  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: "rgba(94, 132, 226, 0.3)",
  },
});
```

# #End

</details>

<details>
  <summary>12. Adding Timer Feature (Component) </summary>

# Adding Timer Feature (Component)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState(null);

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <Focus addSubject={setCurrentSubject} />
      ) : (
        <View>
          <Text style={styles.text}>
            I am going to render the timer for {currentSubject}
          </Text>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => {}}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React from "react";
import { View, Text } from "react-native";

export const Timer = ({ focusSubject }) => (
  <View>
    <Text>Focus Feature {focusSubject}</Text>
  </View>
);
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";
import { spacing, fontSizes } from "../utils/sizes";
import { RoundedButton } from "../components/RoundedButton";

const Focus = ({ addSubject }) => {
  const [subject, setSubject] = useState("");

  const Label = <Text>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.textInput}
          onChangeText={(e) => setSubject(e)}
        />
        <View style={styles.button}>
          <RoundedButton
            title={"+"}
            size={50}
            onPress={() => addSubject(subject)}
          />
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.black500,
  },
  inputContainer: {
    padding: spacing.lg,
    justifyContent: "flex-start",
    flexDirection: "row",
  },
  textInput: {
    flex: 1,
    marginRight: spacing.sm,
    color: colors.white900,
    borderBottomLeftRadius: spacing.sm,
    borderBottomRightRadius: spacing.sm,
    borderTopLeftRadius: spacing.sm,
    borderTopRightRadius: spacing.sm,
    overflow: "hidden",
  },
  button: {
    justifyContent: "center",
  },
});

export default Focus;
```

# #End

</details>

<details>
  <summary>13. Hooking CountDown into Timer Component </summary>

# Hooking CountDown into Timer Component

![](https://github.com/omeatai/My-Tutorials/assets/32337103/b1252fcd-56ad-4978-997f-7ccc40e27d2b)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/d736aad2-7a2b-4839-8f3f-2930f2950222)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <Focus addSubject={setCurrentSubject} />
      ) : (
        <View>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => {}}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";

export const Timer = ({ focusSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  return (
    <View style={styles.container}>
      <View style={styles.countdown}>
        <Countdown
          isPaused={!isStarted}
          onProgress={() => {}}
          onEnd={() => {}}
        />
      </View>
      <View style={styles.buttonWrapper}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    // flex: 1,
  },
  countdown: {
    // flex: 0.5,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 50,
    padding: 15,
  },
  buttonWrapper: {
    // flex: 0.3,
    flexDirection: "row",
    padding: 15,
    justifyContent: "center",
    alignItems: "center",
    marginTop: 100,
  },
});
```

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import colors from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);

export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd();
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;

  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: colors.black500,
  },
});
```

# #End

</details>

<details>
  <summary>14. Adding the Focus Subject </summary>

# Adding the Focus Subject

![](https://github.com/omeatai/My-Tutorials/assets/32337103/eb27894e-acdf-4aff-a8af-aba83f2ae6fd)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/4fa43139-8fe8-48aa-8269-e914d194cbc9)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <Focus addSubject={setCurrentSubject} />
      ) : (
        <View>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => {}}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform } from "react-native";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

export const Timer = ({ focusSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  return (
    <View style={styles.container}>
      <View style={styles.countdown}>
        <Countdown
          isPaused={!isStarted}
          onProgress={() => {}}
          onEnd={() => {}}
        />
      </View>
      <View style={styles.focussubject}>
        <Text style={styles.title}>Focusing on:</Text>
        <Text style={styles.task}>{focusSubject}</Text>
      </View>
      <View style={styles.buttonWrapper}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    // flex: 1,
  },
  countdown: {
    // flex: 0.5,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 50,
    padding: 15,
  },
  buttonWrapper: {
    // flex: 0.3,
    flexDirection: "row",
    padding: 15,
    justifyContent: "center",
    alignItems: "center",
    marginTop: 100,
  },
  focussubject: {
    paddingTop: spacing.xxl,
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import colors from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);

export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd();
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;

  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: colors.black500,
  },
});
```

# #End

</details>

<details>
  <summary>15. Adding the Progress Bar </summary>

# Adding the Progress Bar

![](https://github.com/omeatai/My-Tutorials/assets/32337103/d6614f35-f881-417c-8b6a-5e4ecbd2ed04)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/bd6e5b5f-a332-4114-a37d-75fa035e41d3)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={{ flex: 1 }} style={styles.text}>
        FocusTime App
      </Text>
      {!currentSubject ? (
        <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => {}}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/App.styles.js:

```js
import { StyleSheet, Platform, StatusBar } from "react-native";
import colors from "./src/utils/colors";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  text: {
    color: colors.white900,
    paddingBottom: 20,
    paddingLeft: 20,
    fontWeight: Platform.OS === "android" ? "normal" : "400",
  },
});

export default styles;
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform } from "react-native";
import { ProgressBar } from "react-native-paper";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

export const Timer = ({ focusSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);

  return (
    <View style={styles.container}>
      <View style={styles.countdown}>
        <Countdown
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={() => {}}
        />
        <View style={styles.focussubject}>
          <Text style={styles.title}>Focusing on:</Text>
          <Text style={styles.task}>{focusSubject}</Text>
        </View>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
        <View style={styles.buttonWrapper}>
          {!isStarted && (
            <RoundedButton title="start" onPress={() => setIsStarted(true)} />
          )}
          {isStarted && (
            <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
          )}
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: "auto",
    marginRight: "auto",
  },
  countdown: {
    flex: 2,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 50,
    padding: 15,
  },
  focussubject: {
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 3,
  },
  progressBar: {
    height: spacing.sm,
    marginLeft: "auto",
    marginRight: "auto",
  },
  buttonWrapper: {
    flex: 1,
    flexDirection: "row",
    paddingBottom: 15,
    justifyContent: "center",
    alignItems: "flex-start",
    margin: 100,
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import colors from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);

export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd();
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;

  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: colors.black500,
  },
});
```

### rn/FocusTime/src/utils/colors.js:

```js
const colors = {
  dodgerBlue: "#1e90ff",
  crimson: "#dc143c",
  purple: "#800080",
  darkPurple: "#4d004d",
  white: "#fff",
  white900: "#858585",
  black: "#000",
  black500: "#292929",
  black200: "#5c5c5c",
  black100: "#7a7a7a",
  primary: "#1e90ff",
  secondary: "#000",
  orange500: "#ff6500",
};

export default colors;
```

# #End

</details>

<details>
  <summary>16. Vibrating when Timer Ends </summary>

# Vibrating when Timer Ends

![](https://github.com/omeatai/My-Tutorials/assets/32337103/fdc0306f-3c49-47c6-b92b-785e824b8542)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/087fc695-b777-4838-93ea-ade609492591)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={{ flex: 1 }} style={styles.text}>
        FocusTime App
      </Text>
      {!currentSubject ? (
        <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => {}}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  return (
    <View style={styles.container}>
      <View style={styles.countdown}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={() => {
            Vibration.vibrate(PATTERN);
            setMinutes(0);
          }}
        />
        <View style={styles.focussubject}>
          <Text style={styles.title}>Focusing on:</Text>
          <Text style={styles.task}>{focusSubject}</Text>
        </View>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
        <View style={styles.buttonWrapper}>
          {!isStarted && (
            <RoundedButton title="start" onPress={() => setIsStarted(true)} />
          )}
          {isStarted && (
            <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
          )}
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: "auto",
    marginRight: "auto",
  },
  countdown: {
    flex: 2,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 50,
    padding: 15,
  },
  focussubject: {
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 3,
  },
  progressBar: {
    height: spacing.sm,
    marginLeft: "auto",
    marginRight: "auto",
  },
  buttonWrapper: {
    flex: 1,
    flexDirection: "row",
    paddingBottom: 15,
    justifyContent: "center",
    alignItems: "flex-start",
    margin: 100,
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

# #End

</details>

<details>
  <summary>17. Adding Timer Controls </summary>

# Adding Timer Controls

![](https://github.com/omeatai/My-Tutorials/assets/32337103/2581278a-1546-4a20-b3b3-a6808a1fb485)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/ceb9a399-de77-4efb-8788-e5b3d98ad49f)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={{ flex: 1 }} style={styles.text}>
        FocusTime App
      </Text>
      {!currentSubject ? (
        <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.5);

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={() => {
            Vibration.vibrate(PATTERN);
            setMinutes(0);
          }}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.title}>Focusing on:</Text>
        <Text style={styles.task}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: "auto",
    marginRight: "auto",
  },
  countdownView: {
    flex: 0.4,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    margin: 10,
  },
  focusSubjectView: {
    flex: 0.1,
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 0.1,
    marginTop: 20,
  },
  progressBar: {
    height: spacing.sm,
    flexDirection: "row",
    justifyContent: "center",
  },
  timingWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    paddingTop: spacing.sm,
  },
  buttonWrapperView: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxxl,
    marginBottom: 120,
  },
  clearSubjectWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

### rn/FocusTime/src/features/Timing.js:

```js
import React from "react";
import { View, StyleSheet } from "react-native";
import { RoundedButton } from "../components/RoundedButton";

export const Timing = ({ onChangeTime }) => {
  return (
    <>
      <View style={styles.timingButton}>
        <RoundedButton size={75} title="10" onPress={() => onChangeTime(10)} />
      </View>
      <View style={styles.timingButton}>
        <RoundedButton size={75} title="15" onPress={() => onChangeTime(15)} />
      </View>
      <View style={styles.timingButton}>
        <RoundedButton size={75} title="20" onPress={() => onChangeTime(20)} />
      </View>
    </>
  );
};

const styles = StyleSheet.create({
  timingButton: {
    flex: 1,
    alignItems: "center",
  },
});
```

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import colors from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);

export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd();
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;

  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: colors.black500,
  },
});
```

# #End

</details>

<details>
  <summary>18. Resetting the Timer </summary>

# Resetting the Timer

![](https://github.com/omeatai/My-Tutorials/assets/32337103/15e40644-f10b-406d-9ae5-a3027d131b4f)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/293e4e0f-7c11-4ce8-a86d-3adfae9f52a6)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={{ flex: 1 }} style={styles.text}>
        FocusTime App
      </Text>
      {!currentSubject ? (
        <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject }) => {
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  const onEnd = (reset) => {
    Vibration.vibrate(PATTERN);
    setIsStarted(false);
    setProgress(1);
    reset();
  };

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={onEnd}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.title}>Focusing on:</Text>
        <Text style={styles.task}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: "auto",
    marginRight: "auto",
  },
  countdownView: {
    flex: 0.4,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    margin: 10,
  },
  focusSubjectView: {
    flex: 0.1,
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 0.1,
    marginTop: 20,
  },
  progressBar: {
    height: spacing.sm,
    flexDirection: "row",
    justifyContent: "center",
  },
  timingWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    paddingTop: spacing.sm,
  },
  buttonWrapperView: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxxl,
    marginBottom: 120,
  },
  clearSubjectWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

### rn/FocusTime/src/components/CountDown.js:

```js
import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";

import { fontSizes, spacing } from "../utils/sizes";
import colors from "../utils/colors";

const minutesToMillis = (min) => min * 1000 * 60;
const formatTime = (time) => (time < 10 ? `0${time}` : time);

export const Countdown = ({ minutes = 0.1, isPaused, onProgress, onEnd }) => {
  const interval = React.useRef(null);

  const [millis, setMillis] = useState(null);

  const reset = () => setMillis(minutesToMillis(minutes));

  const countDown = () => {
    setMillis((time) => {
      if (time === 0) {
        clearInterval(interval.current);
        onEnd(reset);
        return time;
      }
      const timeLeft = time - 1000;
      return timeLeft;
    });
  };

  useEffect(() => {
    setMillis(minutesToMillis(minutes));
  }, [minutes]);

  useEffect(() => {
    onProgress(millis / minutesToMillis(minutes));
  }, [millis]);

  useEffect(() => {
    if (isPaused) {
      if (interval.current) clearInterval(interval.current);
      return;
    }

    interval.current = setInterval(countDown, 1000);

    return () => clearInterval(interval.current);
  }, [isPaused]);

  const minute = Math.floor(millis / 1000 / 60) % 60;
  const seconds = Math.floor(millis / 1000) % 60;

  return (
    <Text style={styles.text}>
      {formatTime(minute)}:{formatTime(seconds)}
    </Text>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: fontSizes.xxxl,
    fontWeight: "bold",
    color: colors.white,
    padding: spacing.lg,
    backgroundColor: colors.black500,
  },
});
```

# #End

</details>

<details>
  <summary>19. Keeping the App Awake </summary>

# Keeping the App Awake

![](https://github.com/omeatai/My-Tutorials/assets/32337103/bee813ce-244b-47af-835d-0d00b80988d1)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/80a70e0e-6c24-42cc-9739-3361540e79f1)

# Install expo-keep-awake

```jsbs
npm i expo-keep-awake
yarn add expo-keep-awake
```

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");

  return (
    <SafeAreaView style={styles.container}>
      <Text style={{ flex: 1 }} style={styles.text}>
        FocusTime App
      </Text>
      {!currentSubject ? (
        <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/Timer.js:

```jsbs
import { useKeepAwake } from 'expo-keep-awake';

useKeepAwake();
```

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { useKeepAwake } from "expo-keep-awake";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject }) => {
  useKeepAwake();
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  const onEnd = (reset) => {
    Vibration.vibrate(PATTERN);
    setIsStarted(false);
    setProgress(1);
    reset();
  };

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={onEnd}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.title}>Focusing on:</Text>
        <Text style={styles.task}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: "auto",
    marginRight: "auto",
  },
  countdownView: {
    flex: 0.4,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    margin: 10,
  },
  focusSubjectView: {
    flex: 0.1,
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 0.1,
    marginTop: 20,
  },
  progressBar: {
    height: spacing.sm,
    flexDirection: "row",
    justifyContent: "center",
  },
  timingWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    paddingTop: spacing.sm,
  },
  buttonWrapperView: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxxl,
    marginBottom: 120,
  },
  clearSubjectWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

# #End

</details>

<details>
  <summary>20. Create Focus History Feature </summary>

# Create Focus History Feature

![](https://github.com/omeatai/My-Tutorials/assets/32337103/3047842f-cee1-43e2-bb6c-7d6decb1762f)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/c8a99e56-dd6c-4be3-b792-3e8e5f0dc247)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";
import { FocusHistory } from "./src/features/FocusHistory";

import styles from "./App.styles";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");
  const [history, setHistory] = useState([]);

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>FocusTime App</Text>
      {!currentSubject ? (
        <>
          <Focus style={{ flex: 1 }} addSubject={setCurrentSubject} />
          <FocusHistory history={history} />
        </>
      ) : (
        <View style={{ flex: 1 }}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}
```

### rn/FocusTime/src/features/FocusHistory.js:

```js
import React from "react";
import { View, Text } from "react-native";

export const FocusHistory = () => {
  return (
    <View>
      <Text>Focus history will be built here</Text>
    </View>
  );
};
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { useKeepAwake } from "expo-keep-awake";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject }) => {
  useKeepAwake();
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  const onEnd = (reset) => {
    Vibration.vibrate(PATTERN);
    setIsStarted(false);
    setProgress(1);
    reset();
  };

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={onEnd}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.title}>Focusing on:</Text>
        <Text style={styles.task}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "80%",
    marginLeft: "auto",
    marginRight: "auto",
    flexDirection: "column",
    justifyContent: "center",
  },
  countdownView: {
    flex: 0.3,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    margin: 10,
  },
  focusSubjectView: {
    flex: 0.1,
    paddingTop: spacing.xxl,
  },
  progressBarView: {
    flex: 0.05,
    marginTop: 20,
  },
  progressBar: {
    height: spacing.sm,
    flexDirection: "row",
    justifyContent: "center",
  },
  timingWrapper: {
    flex: 0.05,
    flexDirection: "row",
    justifyContent: "center",
    paddingTop: spacing.sm,
  },
  buttonWrapperView: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxxl,
    marginBottom: 120,
  },
  clearSubjectWrapper: {
    flex: 0.1,
    flexDirection: "row",
    justifyContent: "center",
  },
  title: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  task: { color: colors.white, textAlign: "center" },
});
```

# #End

</details>

<details>
  <summary>21. Styling App and Focus History List </summary>

# Styling App and Focus History List

![](https://github.com/omeatai/My-Tutorials/assets/32337103/44597984-d9ef-4172-ba51-a3dff04ea082)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/3a940172-3173-42a5-9de9-812f449fc90a)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";
import { FocusHistory } from "./src/features/FocusHistory";
import colors from "./src/utils/colors";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");
  const [history, setHistory] = useState([
    "temp feature focused",
    "cook food",
    "drink water",
  ]);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.headingView}>
        <Text style={styles.heading}>FocusTime App</Text>
      </View>

      {!currentSubject ? (
        <View style={styles.focusView}>
          <View style={styles.focusWrapperView}>
            <Focus addSubject={setCurrentSubject} />
          </View>
          <View style={styles.focusHistoryWrapperView}>
            <FocusHistory history={history} />
          </View>
        </View>
      ) : (
        <View style={styles.timerView}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={() => {}}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  headingView: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
    alignContent: "center",
  },
  heading: {
    color: colors.white900,
    fontWeight: Platform.OS === "android" ? "normal" : "700",
  },
  focusView: {
    flex: 19,
    backgroundColor: colors.black500,
  },
  focusWrapperView: {
    flex: 1,
    marginBottom: 30,
  },
  focusHistoryWrapperView: {
    flex: 9,
  },
  timerView: {
    flex: 19,
  },
});
```

### rn/FocusTime/src/features/FocusHistory.js:

```js
import React from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import colors from "../utils/colors";
import { fontSizes, spacing } from "../utils/sizes";

export const FocusHistory = ({ history }) => {
  if (!history || !history.length) return null;

  const renderItem = ({ item }) => <Text style={styles.item}>- {item}</Text>;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Things we've focused on:</Text>
      <FlatList data={history} renderItem={renderItem} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: spacing.md,
    flex: 1,
  },
  item: {
    fontSize: fontSizes.md,
    color: colors.white,
    paddingTop: spacing.sm,
  },
  title: {
    color: colors.white,
    fontSize: fontSizes.md,
    fontWeight: "bold",
  },
});
```

### rn/FocusTime/src/features/Focus.js:

```js
import React, { useState } from "react";
import { StyleSheet, Text, View, Platform } from "react-native";
import { TextInput } from "react-native-paper";
import colors from "../utils/colors";
import { spacing, fontSizes } from "../utils/sizes";
import { RoundedButton } from "../components/RoundedButton";

const Focus = ({ addSubject }) => {
  const [subject, setSubject] = useState("");

  const Label = <Text>{"What task would you like to do?"}</Text>;

  return (
    <View style={styles.container}>
      <View style={styles.inputContainer}>
        <TextInput
          label={Label}
          style={styles.textInput}
          onChangeText={(e) => setSubject(e)}
        />
        <View style={styles.button}>
          <RoundedButton
            title={"+"}
            size={50}
            onPress={() => addSubject(subject)}
          />
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  inputContainer: {
    padding: spacing.lg,
    justifyContent: "flex-start",
    flexDirection: "row",
  },
  textInput: {
    flex: 1,
    marginRight: spacing.sm,
    color: colors.white900,
    borderBottomLeftRadius: spacing.sm,
    borderBottomRightRadius: spacing.sm,
    borderTopLeftRadius: spacing.sm,
    borderTopRightRadius: spacing.sm,
    overflow: "hidden",
  },
  button: {
    justifyContent: "center",
  },
});

export default Focus;
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { useKeepAwake } from "expo-keep-awake";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject }) => {
  useKeepAwake();
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  const onEnd = (reset) => {
    Vibration.vibrate(PATTERN);
    setIsStarted(false);
    setProgress(1);
    reset();
  };

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={onEnd}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.focustitle}>Focusing on:</Text>
        <Text style={styles.focustask}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "80%",
    marginLeft: "auto",
    marginRight: "auto",
    justifyContent: "space-around",
  },
  countdownView: {
    flex: 3,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  focusSubjectView: {
    flex: 1,
  },
  focustitle: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  focustask: { color: colors.white, textAlign: "center" },
  progressBarView: {
    flex: 1,
  },
  progressBar: {
    height: spacing.sm,
  },
  timingWrapper: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
  },
  buttonWrapperView: {
    flex: 2,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxl,
    marginBottom: spacing.xxl,
  },
  clearSubjectWrapper: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
  },
});
```

# #End

</details>

<details>
  <summary>22. Populating the Focus History List </summary>

# Populating the Focus History List

![](https://github.com/omeatai/My-Tutorials/assets/32337103/081b7da7-f9e2-4ce4-821d-cc7ca40bdad3)
![](https://github.com/omeatai/My-Tutorials/assets/32337103/38055aea-d6a5-44a1-9ec0-e42ccb62a4a4)

### rn/FocusTime/App.js:

```js
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  Platform,
  StatusBar,
} from "react-native";

import Focus from "./src/features/Focus";
import { Timer } from "./src/features/Timer";
import { FocusHistory } from "./src/features/FocusHistory";
import colors from "./src/utils/colors";

export default function App() {
  const [currentSubject, setCurrentSubject] = useState("Wash Plate");
  const [history, setHistory] = useState([]);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.headingView}>
        <Text style={styles.heading}>FocusTime App</Text>
      </View>

      {!currentSubject ? (
        <View style={styles.focusView}>
          <View style={styles.focusWrapperView}>
            <Focus addSubject={setCurrentSubject} />
          </View>
          <View style={styles.focusHistoryWrapperView}>
            <FocusHistory history={history} />
          </View>
        </View>
      ) : (
        <View style={styles.timerView}>
          <Timer
            focusSubject={currentSubject}
            onTimerEnd={(subject) => {
              setHistory([...history, subject]);
            }}
            clearSubject={() => setCurrentSubject(null)}
          />
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight + 5 : 0,
    backgroundColor: colors.black,
  },
  headingView: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
    alignContent: "center",
  },
  heading: {
    color: colors.white900,
    fontWeight: Platform.OS === "android" ? "normal" : "700",
  },
  focusView: {
    flex: 19,
    backgroundColor: colors.black500,
  },
  focusWrapperView: {
    flex: 2,
  },
  focusHistoryWrapperView: {
    flex: 8,
  },
  timerView: {
    flex: 19,
  },
});
```

### rn/FocusTime/src/features/FocusHistory.js:

```js
import React from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import colors from "../utils/colors";
import { fontSizes, spacing } from "../utils/sizes";

export const FocusHistory = ({ history }) => {
  if (!history || !history.length)
    return (
      <View style={styles.container}>
        <Text style={styles.title}>We haven't focused on anything yet!</Text>
      </View>
    );

  const renderItem = ({ item }) => <Text style={styles.item}>- {item}</Text>;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Things we've focused on:</Text>
      <FlatList data={history} renderItem={renderItem} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: spacing.md,
    flex: 1,
    alignItems: "center",
  },
  item: {
    fontSize: fontSizes.md,
    color: colors.white,
    paddingTop: spacing.sm,
  },
  title: {
    color: colors.white,
    fontSize: fontSizes.md,
    fontWeight: "bold",
  },
});
```

### rn/FocusTime/src/features/Timer.js:

```js
import React, { useState } from "react";
import { View, Text, StyleSheet, Platform, Vibration } from "react-native";
import { ProgressBar } from "react-native-paper";
import { useKeepAwake } from "expo-keep-awake";
import { Countdown } from "../components/CountDown";
import { RoundedButton } from "../components/RoundedButton";
import { Timing } from "./Timing";
import { spacing } from "../utils/sizes";
import colors from "../utils/colors";

const ONE_SECOND_IN_MS = 1000;

const PATTERN = [
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
  1 * ONE_SECOND_IN_MS,
];

export const Timer = ({ focusSubject, clearSubject, onTimerEnd }) => {
  useKeepAwake();
  const [isStarted, setIsStarted] = useState(false);
  const [progress, setProgress] = useState(1);
  const [minutes, setMinutes] = useState(0.1);

  const onEnd = (reset) => {
    Vibration.vibrate(PATTERN);
    setIsStarted(false);
    setProgress(1);
    reset();
    onTimerEnd(focusSubject);
  };

  return (
    <View style={styles.container}>
      <View style={styles.countdownView}>
        <Countdown
          minutes={minutes}
          isPaused={!isStarted}
          onProgress={(progress) => {
            setProgress(progress);
          }}
          onEnd={onEnd}
        />
      </View>

      <View style={styles.focusSubjectView}>
        <Text style={styles.focustitle}>Focusing on:</Text>
        <Text style={styles.focustask}>{focusSubject}</Text>
      </View>

      <View style={styles.progressBarView}>
        <ProgressBar
          style={styles.progressBar}
          progress={progress}
          color={colors.orange500}
        />
      </View>

      <View style={styles.timingWrapper}>
        <Timing onChangeTime={setMinutes} />
      </View>

      <View style={styles.buttonWrapperView}>
        {!isStarted && (
          <RoundedButton title="start" onPress={() => setIsStarted(true)} />
        )}
        {isStarted && (
          <RoundedButton title="pause" onPress={() => setIsStarted(false)} />
        )}
      </View>

      <View style={styles.clearSubjectWrapper}>
        <RoundedButton size={50} title="-" onPress={clearSubject} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "80%",
    marginLeft: "auto",
    marginRight: "auto",
    justifyContent: "space-around",
  },
  countdownView: {
    flex: 3,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  focusSubjectView: {
    flex: 1,
  },
  focustitle: {
    color: colors.white,
    textAlign: "center",
    fontWeight: Platform.OS === "android" ? "bold" : "900",
  },
  focustask: { color: colors.white, textAlign: "center" },
  progressBarView: {
    flex: 1,
  },
  progressBar: {
    height: spacing.sm,
  },
  timingWrapper: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
  },
  buttonWrapperView: {
    flex: 2,
    flexDirection: "row",
    justifyContent: "center",
    marginTop: spacing.xxl,
    marginBottom: spacing.xxl,
  },
  clearSubjectWrapper: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
  },
});
```

# #End

</details>

<details>
  <summary>23. Run FocusTIme on Mac </summary>

# Run FocusTIme on Mac

# Install git

```jsbs
brew install git
```

# Prepare code for Github repository

```jsbs
git add .
git commit -am "initial"
```

# Check requirements

```jsbs
echo $PATH
node -v
npm -v
yarn -v
```

# Install dependencies

```jsbs
yarn
yarn install
```

# Install expo-cli

```jsbs
sudo npm install -g expo-cli
```

### rn/focustimeproject/package.json:

```js
{
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "expo": "~47.0.14",
    "expo-status-bar": "~1.4.2",
    "react": "18.1.0",
    "react-native": "0.70.8",
    "expo-constants": "~14.0.2",
    "@expo/vector-icons": "^13.0.0",
    "react-native-paper": "4.11.2",
    "expo-keep-awake": "~11.0.1"
  },
  "devDependencies": {
    "@babel/core": "^7.12.9"
  },
  "private": true
}
```

# Run expo on xcode simulator

```jsbs
yarn ios
```

![](https://github.com/omeatai/My-Tutorials/assets/32337103/39743fac-9c33-4724-8f14-ce4511d43b13)

# Run expo on android simulator

```jsbs
yarn android
```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

</details>
