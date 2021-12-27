import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

class Frauds extends StatefulWidget {
  const Frauds({Key? key}) : super(key: key);

  @override
  _FraudsState createState() => _FraudsState();
}

class _FraudsState extends State<Frauds> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Lottie.asset(
        'assets/JSON/comingSoon.json',
        height: 250.0,
        width: 250.0,
      ),
    );
  }
}
