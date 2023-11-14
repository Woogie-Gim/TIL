<template>
  <div class="home">
    <h1>home</h1>
    <div>
      <button v-on:click="test">axios 테스트</button>
    </div>
    <div>
      <div class="id-input-wrapper">
        <input type="text" v-model="userid" />
      </div>
      <div class="password-input-wrapper">
        <input type="password" v-model="userpw" />
      </div>
      <button v-on:click="login">로그인</button>
    </div>
    <div>
      <button v-on:click="logout">로그아웃</button>
    </div>
    <div>
      <h2>회원가입</h2>
      <div>
        <input type="text" v-model="signupID" placeholder="아이디를 입력하세요">
      </div>
      <div>
        <input type="password" v-model="signupPW1" placeholder="비밀번호를 입력하세요">
      </div>
      <div>
        <input type="password" v-model="signupPW2" placeholder="비밀번호를 다시 입력하세요" />
      </div>
      <button v-on:click="signup">회원가입</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const userid = ref('');
    const userpw = ref('');
    const signupID = ref('');
    const signupPW1 = ref('');
    const signupPW2 = ref('');
    const URL = "http://localhost:8000/";
    const TOKEN = ref('');

    const test = () => {
      axios.get('${URL}api/v1/articles/', {
        headers: {
          Authorization: 'Token ${TOKEN.value}',
        },
      }).then(response => {
        if (response.data) {
          console.log(response.data);
        }
      }).catch(error => {
        console.error(error);
      });
    };

    const login = () => {
      console.log(userid.value);
      console.log(userpw.value);
      axios.post('${URL}accounts/login/', {
        username: userid.value,
        password: userpw.value,
      }).then(response => {
        if (response.data) {
          console.log(response.data);
          TOKEN.value = response.data.key;
        }
      }).catch(error => {
        console.error(error);
      });
    };

    const logout = () => {
      axios.post('${URL}accounts/logout/').then(response => {
        if (response.data) {
          console.log(response.data);
          TOKEN.value = '';
        }
      }).catch(error => {
        console.error(error);
      });
    };

    const signup = () => {
      if (signupPW1.value !== signupPW2.value) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
      }

      axios.post('${URL}accounts/signup/', {
        username: signupID.value,
        password1: signupPW1.value,
        password2: signupPW2.value,
      }).then(response => {
        console.log(response.data);
        TOKEN.value = response.data.key;
      }).catch(error => {
        console.error(error);
      });
    };

    return { userid, userpw, signupID, signupPW1, signupPW2, URL, TOKEN, test, login, logout, signup };
  },
};
</script>