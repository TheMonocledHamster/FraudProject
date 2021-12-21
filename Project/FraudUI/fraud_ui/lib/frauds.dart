import 'package:flutter/material.dart';

class Frauds extends StatefulWidget {
  const Frauds({Key? key}) : super(key: key);

  @override
  _FraudsState createState() => _FraudsState();
}

class _FraudsState extends State<Frauds> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: Text('frauds'),
      ),
    );
  }
}
