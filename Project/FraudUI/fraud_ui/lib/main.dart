import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final List<String> _titles = [
    'Home',
    'Stats',
    'Frauds',
    'Queries',
  ];
  final List<Widget> _icons = [
    Icon(Icons.home),
    Icon(Icons.grade),
    Icon(Icons.person),
    Icon(Icons.save),
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: <Widget>[
          ListView.builder(itemBuilder: (context, i) {
            return ListTile(
              title: Text(_titles[i]),
              leading: _icons[i],
            );
          }),
        ],
      ),
    );
  }
}
