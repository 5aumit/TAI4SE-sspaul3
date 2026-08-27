package devy.jwt.sqlite.jpa.controller;

import devy.jwt.sqlite.jpa.domain.Member;
import devy.jwt.sqlite.jpa.request.MemberSigninRequest;
import devy.jwt.sqlite.jpa.request.MemberSignupRequest;
import devy.jwt.sqlite.jpa.response.Response;
import devy.jwt.sqlite.jpa.service.MemberService;
import devy.jwt.sqlite.jpa.valid.MemberSigninValidator;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import devy.jwt.sqlite.jpa.valid.MemberSignupValidator;

import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import java.util.List;

/**
 * 회원 컨트롤러
 */
@RestController
@RequestMapping("/member")
public class MemberController {

    private final MemberService memberService;

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    /**
     * 회원 정보 등록
     * @param memberSignupRequest 회원정보
     * @param bindingResult 유효성 검사 결과
     * @return 등록된 회원정보
     * @see MemberSignupRequest
     * @see MemberSignupValidator
     */
    @PostMapping("/signup")
    public Response signup(@Valid @RequestBody MemberSignupRequest memberSignupRequest, BindingResult bindingResult) {
        // 입력한 회원정보의 유효성 검사`
        new MemberSignupValidator(memberService).validate(memberSignupRequest, bindingResult);

        // 유효성 검사를 통과하지 못하면 회원정보를 등록하지 않고 결과를 반환한다
        if(bindingResult.hasErrors()) {
            return new Response(bindingResult);
        }

        // 회원정보 등록
        Member signupMember = memberService.signup(memberSignupRequest.toMember());

        // 결과
        return new Response(signupMember);
    }

    /**
     * 로그인
     * @param memberSigninRequest 로그인 정보
     * @param bindingResult 유효성 검사 결과
     * @param response jwt를 헤더에 담기 위한 HttpServletResponse 객체
     * @return 헤더에 jwt가 담겨 있으므로 응답 body에는 어떠한 데이터도 담지 않는다
     * @see MemberSigninRequest
     * @see MemberSigninValidator
     */
    @PostMapping("/signin")
    public Response signin(@Valid @RequestBody MemberSigninRequest memberSigninRequest, BindingResult bindingResult, HttpServletResponse response) {
        // 입력한 회원정보의 유효성 검사
        new MemberSigninValidator(memberService).validate(memberSigninRequest, bindingResult);

        // 유효성 검사를 통과하지 못하면 jwt를 생성하지 않고 결과를 반환한다
        if(bindingResult.hasErrors()) {
            return new Response(bindingResult);
        }

        // jwt 생성
        String jwt = memberService.signin(memberSigninRequest.toMember());

        // 헤더에 담아 전송
        response.addHeader("Authorization", jwt);

        // 결과
        return new Response();
    }

    @GetMapping("/list/all")
    public Response memberListAll() {
        return new Response(memberService.getMemberListAll());
    }

}
